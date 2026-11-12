import glob
import re

links = []
total_count = 0
for ext in ['html', 'js']:
    for f in glob.glob(f'**/*.{ext}', recursive=True):
        if 'work' in f or '.codex' in f:
            continue
        content = open(f, encoding='utf-8', errors='ignore').read()
        matches = re.findall(r'href=[\'"][^\'"]*class\.html[^\'"]*[\'"]', content)
        if matches:
            links.append((f, len(matches)))
            total_count += len(matches)

print(f"Total files linking to class.html: {len(links)}")
print(f"Total internal links to class.html: {total_count}")
for f, count in sorted(links, key=lambda x: -x[1]):
    print(f"  {f}: {count} links")
