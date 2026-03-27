import os, re
from datetime import date

version = date.today().strftime("%Y%m%d")

html_files = [f for f in os.listdir('.') if f.endswith('.html')]
updated = 0
for fname in html_files:
    with open(fname, 'r', encoding='utf-8') as f:
        content = f.read()
    new_content = re.sub(r'href="style\.css(?:\?v=\d+)?"', f'href="style.css?v={version}"', content)
    if new_content != content:
        with open(fname, 'w', encoding='utf-8') as f:
            f.write(new_content)
        updated += 1

print(f"Bumped to v={version} across {updated} HTML files.")
