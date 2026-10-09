"""Convert an Outlook e-mail body (HTML, as returned by the Microsoft 365 connector's
read_resource call) into a Markdown source file with front matter.

Usage:
    python3 -I tools/mail_html_to_md.py <body.html> --out sources/emails/<file>.md \
        --date 2026-09-25 --subject "..." --from "Ahmet Gunduz <agunduz@multi.eu>" \
        --to "Country FDs ..." [--cc "..."] --status current [--superseded-by <file>] \
        --topics closing-calendar,control-file --weblink <outlook url> \
        [--message-id <id>] [--attachments "a.pdf; b.xlsx"] [--note "..."] [--strip-quoted]

--strip-quoted cuts the converted text at the first quoted-mail header
("From: ... Sent: ...") so that replies do not carry the whole thread.
The HTML -> Markdown conversion reuses tools/wiki_to_md.py (standard library only).
"""
import argparse
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from wiki_to_md import html_to_md  # noqa: E402


def strip_quoted(md: str) -> str:
    lines = md.splitlines()
    for i, line in enumerate(lines):
        if re.match(r"^\**\s*(From|Da|Von|De):\**\s", line.strip()):
            window = "\n".join(lines[i:i + 4])
            if re.search(r"\**\s*(Sent|Inviato|Gesendet|Envoy\S*|Enviado):\**", window):
                return "\n".join(lines[:i]).rstrip() + "\n\n*(quoted earlier messages removed)*\n"
    return md


def yaml_str(s: str) -> str:
    s = (s or "").replace("\\", "\\\\").replace('"', '\\"')
    return f'"{s}"'


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("html")
    ap.add_argument("--out", required=True)
    ap.add_argument("--date", required=True)
    ap.add_argument("--subject", required=True)
    ap.add_argument("--from", dest="sender", required=True)
    ap.add_argument("--to", default="")
    ap.add_argument("--cc", default="")
    ap.add_argument("--status", default="current", choices=["current", "superseded", "obsolete", "reference"])
    ap.add_argument("--superseded-by", default="")
    ap.add_argument("--topics", default="")
    ap.add_argument("--weblink", default="")
    ap.add_argument("--message-id", default="")
    ap.add_argument("--attachments", default="")
    ap.add_argument("--note", default="")
    ap.add_argument("--strip-quoted", action="store_true")
    a = ap.parse_args()

    with open(a.html, encoding="utf-8", errors="replace") as f:
        raw = f.read()
    md, links, images = html_to_md(raw)
    md = re.sub(r"!\[[^\]]*\]\(cid:[^)]*\)", "", md)  # inline images (logos)
    md = re.sub(r"\n{3,}", "\n\n", md).strip() + "\n"
    if a.strip_quoted:
        md = strip_quoted(md)

    topics = ", ".join(t.strip() for t in a.topics.split(",") if t.strip())
    front = [
        "---",
        f"date: {a.date}",
        f"subject: {yaml_str(a.subject)}",
        f"from: {yaml_str(a.sender)}",
        f"to: {yaml_str(a.to)}",
    ]
    if a.cc:
        front.append(f"cc: {yaml_str(a.cc)}")
    front += [
        f"status: {a.status}",
        f"superseded_by: {a.superseded_by}",
        f"topics: [{topics}]",
        f"outlook: {yaml_str(a.weblink)}",
    ]
    if a.message_id:
        front.append(f"message_id: {yaml_str(a.message_id)}")
    if a.attachments:
        front.append(f"attachments: {yaml_str(a.attachments)}")
    front.append("fetched: 2026-10-09 via Microsoft 365 connector (read-only)")
    front.append("---")
    body = "\n".join(front) + "\n\n"
    if a.note:
        body += f"> {a.note}\n\n"
    body += md
    os.makedirs(os.path.dirname(os.path.abspath(a.out)), exist_ok=True)
    with open(a.out, "w", encoding="utf-8") as f:
        f.write(body)
    print(f"OK {a.out} ({len(md.split())} words, {len(links)} links)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
