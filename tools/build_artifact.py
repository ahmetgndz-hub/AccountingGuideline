"""Build the site for publishing as a Claude artifact (multi-file page).

Produces, under <out-dir>:
  site-artifact/        every page as <name>.html (no directory URLs), assets, search index
  artifact-root.html    the home page adapted to the artifact skeleton (no doctype/html/head/body)

Usage:
    python3 tools/build_artifact.py <out-dir>

Then publish artifact-root.html with the files under site-artifact/ to the existing
artifact URL (see docs/how-to-update.md).
"""
import os
import pathlib
import re
import subprocess
import sys

REPO = pathlib.Path(__file__).resolve().parent.parent


def main() -> int:
    out = pathlib.Path(sys.argv[1]).resolve()
    out.mkdir(parents=True, exist_ok=True)
    site = out / "site-artifact"

    cfg = (REPO / "mkdocs.yml").read_text(encoding="utf-8")
    cfg = re.sub(r"^site_url:.*\n", "", cfg, flags=re.M)
    cfg = re.sub(r"^edit_uri:.*\n", "", cfg, flags=re.M)
    cfg += f"\ndocs_dir: {REPO / 'docs'}\nuse_directory_urls: false\nsite_dir: {site}\n"
    cfg_path = out / "mkdocs-artifact.yml"
    cfg_path.write_text(cfg, encoding="utf-8")
    subprocess.run(["mkdocs", "build", "--strict", "-f", str(cfg_path)], check=True)

    for p in list(site.rglob("*")):
        if p.is_file() and (p.suffix in (".map", ".gz") or p.name in ("sitemap.xml", "404.html", "objects.inv")):
            p.unlink()

    html = (site / "index.html").read_text(encoding="utf-8")
    head = re.search(r"<head>(.*?)</head>", html, re.S).group(1)
    body_m = re.search(r"<body([^>]*)>(.*)</body>", html, re.S)
    body_attrs, body = body_m.group(1), body_m.group(2)
    head = re.sub(r'<meta charset[^>]*>', "", head)
    head = re.sub(r'<meta name="viewport"[^>]*>', "", head)
    head = re.sub(r'<link rel="canonical"[^>]*>', "", head)
    title_m = re.search(r"<title>(.*?)</title>", head, re.S)
    head = head.replace(title_m.group(0), "")
    attrs = dict(re.findall(r'([\w-]+)="([^"]*)"', body_attrs))
    setter = "<script>(function(){var b=document.body;" + "".join(
        f"b.setAttribute({a!r},{v!r});" for a, v in attrs.items()) + "})();</script>"
    (out / "artifact-root.html").write_text(
        f"<title>{title_m.group(1).strip()}</title>\n{head}\n{setter}\n{body}\n", encoding="utf-8")
    (site / "index.html").unlink()

    files = sorted(str(p.relative_to(site)).replace(os.sep, "/") for p in site.rglob("*") if p.is_file())
    (out / "artifact-files.txt").write_text("\n".join(files) + "\n", encoding="utf-8")
    print(f"{len(files)} files under {site}; root page {out / 'artifact-root.html'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
