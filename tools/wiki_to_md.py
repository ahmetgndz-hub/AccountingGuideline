"""Convert exported SharePoint Enterprise Wiki pages (.aspx) to Markdown.

The pages come from downloading the `Paginas` library of
https://multieu.sharepoint.com/sites/Wiki as a zip. Each .aspx holds the page
body HTML-escaped inside <mso:PublishingPageContent>. This script extracts it,
converts it to Markdown with the standard library only, and writes one file per
page plus an INDEX.md.

Usage:
    python3 -I tools/wiki_to_md.py <extracted-zip-dir> <output-dir>
"""
import datetime as dt
import html
import os
import re
import sys
from html.parser import HTMLParser


# --------------------------------------------------------------------------- #
# HTML -> Markdown
# --------------------------------------------------------------------------- #
class MarkdownConverter(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.out = []
        self.list_stack = []
        self.href = None
        self.in_table = 0
        self.row = None
        self.cell = None
        self.rows_in_table = 0
        self.skip = 0
        self.pre = False
        self.images = []
        self.links = []

    def _emit(self, s):
        if self.cell is not None:
            self.cell.append(s)
        else:
            self.out.append(s)

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag in ("script", "style"):
            self.skip += 1
            return
        if self.skip:
            return
        if tag in ("h1", "h2", "h3", "h4", "h5", "h6"):
            if self.cell is None and not self.list_stack:
                self._emit("\n\n" + "#" * int(tag[1]) + " ")
            else:
                self._emit("**")
        elif tag == "p":
            self._emit("\n\n" if self.cell is None else " ")
        elif tag == "br":
            self._emit("\n" if self.cell is None else " ")
        elif tag == "hr":
            self._emit("\n\n---\n\n")
        elif tag in ("strong", "b"):
            self._emit("**")
        elif tag in ("em", "i"):
            self._emit("*")
        elif tag == "pre":
            self.pre = True
            self._emit("\n\n```\n")
        elif tag == "code" and not self.pre:
            self._emit("`")
        elif tag == "a":
            self.href = a.get("href")
            if self.href:
                self.links.append(self.href)
            self._emit("[")
        elif tag == "img":
            src = a.get("src", "")
            self.images.append(src)
            self._emit(f"![{a.get('alt') or 'image'}]({src})")
        elif tag in ("ul", "ol"):
            self.list_stack.append(tag)
            if self.cell is None:
                self._emit("\n")
        elif tag == "li":
            depth = max(len(self.list_stack) - 1, 0)
            marker = "1." if self.list_stack and self.list_stack[-1] == "ol" else "-"
            if self.cell is None:
                self._emit("\n" + "  " * depth + marker + " ")
            else:
                self._emit(" • ")
        elif tag == "table":
            self.in_table += 1
            if self.in_table == 1:
                self.rows_in_table = 0
                self._emit("\n\n")
        elif tag == "tr" and self.in_table == 1:
            self.row = []
        elif tag in ("td", "th") and self.in_table == 1:
            if self.row is None:  # malformed HTML: cell without a row
                self.row = []
            self.cell = []
        elif tag == "blockquote":
            self._emit("\n\n> ")

    def handle_endtag(self, tag):
        if tag in ("script", "style"):
            self.skip = max(self.skip - 1, 0)
            return
        if self.skip:
            return
        if tag in ("h1", "h2", "h3", "h4", "h5", "h6"):
            self._emit("**" if (self.cell is not None or self.list_stack) else "\n")
        elif tag in ("strong", "b"):
            self._emit("**")
        elif tag in ("em", "i"):
            self._emit("*")
        elif tag == "pre":
            self.pre = False
            self._emit("\n```\n\n")
        elif tag == "code" and not self.pre:
            self._emit("`")
        elif tag == "a":
            self._emit(f"]({self.href or ''})")
            self.href = None
        elif tag in ("ul", "ol"):
            if self.list_stack:
                self.list_stack.pop()
            if self.cell is None:
                self._emit("\n")
        elif tag in ("td", "th") and self.cell is not None:
            text = " ".join("".join(self.cell).split())
            text = re.sub(r"\*\*\s*\*\*", "", text)
            if self.row is None:
                self.row = []
            self.row.append(text.replace("|", "\\|"))
            self.cell = None
        elif tag == "tr" and self.row is not None:
            if any(c.strip() for c in self.row):
                self.out.append("| " + " | ".join(self.row) + " |\n")
                if self.rows_in_table == 0:
                    self.out.append("|" + "---|" * max(len(self.row), 1) + "\n")
                self.rows_in_table += 1
            self.row = None
        elif tag == "table":
            self.in_table = max(self.in_table - 1, 0)
            if self.in_table == 0:
                if self.row:  # flush an unterminated row
                    self.out.append("| " + " | ".join(self.row) + " |\n")
                self.row = None
                self.cell = None
                self.out.append("\n")
        elif tag in ("p", "div", "section"):
            if self.cell is None:
                self._emit("\n")

    def handle_data(self, data):
        if self.skip:
            return
        data = data.replace("​", "")  # zero-width spaces from the RTE
        if self.pre:
            self._emit(data)
        else:
            self._emit(re.sub(r"[ \t\r\n]+", " ", data))

    def result(self) -> str:
        text = "".join(self.out)
        text = re.sub(r"\*\*\s*\*\*", "", text)
        text = re.sub(r"^#{1,6}\s*$", "", text, flags=re.M)
        text = re.sub(r"^(\s*(?:-|\d+\.))\s*\n\s*\n", r"\1 ", text, flags=re.M)
        text = re.sub(r"[ \t]+\n", "\n", text)
        text = re.sub(r"\n{3,}", "\n\n", text)
        return text.strip() + "\n"


def html_to_md(raw_html: str):
    conv = MarkdownConverter()
    conv.feed(raw_html or "")
    return conv.result(), conv.links, conv.images


# --------------------------------------------------------------------------- #
# .aspx parsing
# --------------------------------------------------------------------------- #
def mso_field(src: str, name: str) -> str:
    m = re.search(rf"<mso:{name}[^>]*>(.*?)</mso:{name}>", src, re.S)
    return html.unescape(m.group(1)) if m else ""


def slugify(name: str) -> str:
    s = re.sub(r"\.aspx$", "", name, flags=re.I)
    s = re.sub(r"[^A-Za-z0-9]+", "-", s).strip("-").lower()
    return s or "page"


def main() -> int:
    src_dir, out_dir = sys.argv[1], sys.argv[2]
    os.makedirs(out_dir, exist_ok=True)
    today = dt.date.today().isoformat()
    rows = []

    for root, _, files in os.walk(src_dir):
        for fn in sorted(files):
            if not fn.lower().endswith(".aspx"):
                continue
            path = os.path.join(root, fn)
            rel = os.path.relpath(path, src_dir)
            with open(path, encoding="utf-8-sig", errors="replace") as f:
                src = f.read()
            body = mso_field(src, "PublishingPageContent")
            title = mso_field(src, "Title") or re.sub(r"\.aspx$", "", fn.strip("​"), flags=re.I)
            contact = mso_field(src, "display_urn_x003a_schemas-microsoft-com_x003a_office_x003a_office_x0023_PublishingContact")
            categories = mso_field(src, "Wiki_x0020_Page_x0020_Categories")
            md, links, images = html_to_md(body)
            folder = os.path.dirname(rel).replace(os.sep, "/")
            slug = (slugify(folder) + "--" if folder and folder != "." else "") + slugify(fn.strip("​"))
            if os.path.exists(os.path.join(out_dir, slug + ".md")):
                slug += "-2"  # duplicate page names (e.g. zero-width-space variants)
            words = len(md.split())
            front = (
                "---\n"
                f"title: \"{title.replace(chr(34), chr(39))}\"\n"
                f"source_file: \"{rel}\"\n"
                f"sharepoint: \"https://multieu.sharepoint.com/sites/Wiki/Paginas/{rel.replace(os.sep, '/')}\"\n"
                f"contact: \"{contact}\"\n"
                f"categories: \"{categories}\"\n"
                f"converted: {today}\n"
                "status: old-wiki\n"
                "---\n\n"
            )
            with open(os.path.join(out_dir, slug + ".md"), "w", encoding="utf-8") as f:
                f.write(front + f"# {title}\n\n" + md)
            rows.append((title, slug + ".md", words, len(links), len(images), contact))
            print(f"OK {rel} -> {slug}.md ({words} words, {len(links)} links, {len(images)} images)")

    rows.sort(key=lambda r: r[0].lower())
    with open(os.path.join(out_dir, "INDEX.md"), "w", encoding="utf-8") as f:
        f.write(f"# Old Multi Wiki snapshot ({today})\n\n")
        f.write("Converted from the SharePoint `Paginas` library export. Raw export: "
                "`sources/wiki/OneDrive_1_10-8-2026.zip`. These pages are the *outdated* "
                "baseline; the guideline in `docs/` supersedes them.\n\n")
        f.write("| Page | File | Words | Links | Images | Contact |\n|---|---|---|---|---|---|\n")
        for title, fn, words, nl, ni, contact in rows:
            f.write(f"| {title} | [{fn}]({fn}) | {words} | {nl} | {ni} | {contact} |\n")
    print(f"DONE {len(rows)} pages -> {out_dir}/")
    return 0


if __name__ == "__main__":
    sys.exit(main())
