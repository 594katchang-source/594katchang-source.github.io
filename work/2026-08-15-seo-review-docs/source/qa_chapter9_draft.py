import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).parents[1] / 'output' / 'chapter-09-energy-balance-seo-review.md'
text = path.read_text(encoding='utf-8')
body = text.split('## 4. 正文', 1)[1].split('## 5. SEO 描述', 1)[0]
plain = re.sub(r'!?(?:\[[^\]]*\])\([^)]*\)', '', body)
plain = re.sub(r'[`*_>#|\-]', '', plain)
plain = re.sub(r'\s+', '', plain)
checks = {
    'file_exists': path.exists(),
    'body_characters_at_least_2000': len(plain) >= 2000,
    'has_h1': len(re.findall(r'^# ', text, flags=re.M)) == 1,
    'has_h2': len(re.findall(r'^## ', body, flags=re.M)) >= 8,
    'has_h3': len(re.findall(r'^### ', body, flags=re.M)) >= 3,
    'has_tables': len(re.findall(r'^\|', body, flags=re.M)) >= 10,
    'has_faq': 'FAQ：能量平衡與健康身體常見問題' in body,
    'has_author_judgment': 'Kat Chang 營養師的判讀' in body,
    'has_source_section': '## 10. 來源連結與各來源支持的段落或主張' in text,
    'has_medical_limit': '需要醫療評估' in body or '醫療團隊' in body,
    'forbidden_long_dash_absent': '——' not in text,
    'forbidden_semicolon_absent': '；' not in text,
    'source_urls_present': len(re.findall(r'https?://', text)) >= 8,
}
for key, value in checks.items():
    print(f'{key}: {"PASS" if value else "FAIL"}')
print(f'body_characters_without_whitespace: {len(plain)}')
if not all(checks.values()):
    raise SystemExit(1)
