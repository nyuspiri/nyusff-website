"""Keep every page's shared pieces in sync.

Run after editing partials/header.html, partials/footer.html, style.css or script.js:

    python3 build.py

What it does to each *.html page in this folder:
  - replaces <header class="site-header">…</header> with partials/header.html
  - replaces <footer class="site-footer">…</footer> with partials/footer.html
  - marks the current page's nav link with aria-current="page"
  - points style.css / script.js at a version string based on their contents,
    so browsers pick up changes without a manual cache-bust
"""
import hashlib
import pathlib
import re

ROOT = pathlib.Path(__file__).parent


def file_version(name):
    return hashlib.md5((ROOT / name).read_bytes()).hexdigest()[:8]


def main():
    header = (ROOT / "partials/header.html").read_text(encoding="utf-8").rstrip()
    footer = (ROOT / "partials/footer.html").read_text(encoding="utf-8").rstrip()
    css_v, js_v = file_version("style.css"), file_version("script.js")

    changed = 0
    for page in sorted(ROOT.glob("*.html")):
        html = page.read_text(encoding="utf-8")
        new = html

        page_header = header.replace(
            f'href="{page.name}"', f'href="{page.name}" aria-current="page"'
        )
        new = re.sub(r'[ \t]*<header class="site-header">.*?</header>',
                     lambda _: page_header, new, count=1, flags=re.S)
        new = re.sub(r'[ \t]*<footer class="site-footer">.*?</footer>',
                     lambda _: footer, new, count=1, flags=re.S)
        new = re.sub(r'href="style\.css(\?v=[^"]*)?"', f'href="style.css?v={css_v}"', new)
        new = re.sub(r'<script src="script\.js(\?v=[^"]*)?"( defer)?></script>',
                     f'<script src="script.js?v={js_v}" defer></script>', new)

        if new != html:
            page.write_text(new, encoding="utf-8")
            changed += 1

    print(f"Synced {changed} page(s). style.css v={css_v}, script.js v={js_v}")


if __name__ == "__main__":
    main()
