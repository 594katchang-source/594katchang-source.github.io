import argparse
import json
import re
import sys
from html import unescape
from html.parser import HTMLParser
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

from build_review_docs import build_doc


class MarkdownBodyParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.blocks = []
        self.current = []
        self.block_tag = None
        self.list_tag = None
        self.table = None
        self.row = None
        self.cell = None
        self.cell_tag = None
        self.anchor = None

    def text_target(self):
        if self.cell is not None:
            return self.cell
        return self.current

    def flush_block(self):
        if not self.block_tag:
            return
        value = ''.join(self.current).strip()
        if value:
            if self.block_tag == 'h2':
                self.blocks.append('## ' + value)
            elif self.block_tag == 'h3':
                self.blocks.append('### ' + value)
            elif self.block_tag == 'li':
                prefix = '1. ' if self.list_tag == 'ol' else '- '
                self.blocks.append(prefix + value)
            else:
                self.blocks.append(value)
        self.current = []
        self.block_tag = None

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag in ('p', 'h2', 'h3', 'li'):
            self.flush_block()
            self.block_tag = tag
        elif tag in ('ul', 'ol'):
            self.flush_block()
            self.list_tag = tag
        elif tag == 'table':
            self.flush_block()
            self.table = []
        elif tag == 'tr':
            self.row = []
        elif tag in ('th', 'td'):
            self.cell = []
            self.cell_tag = tag
        elif tag == 'a':
            self.anchor = attrs.get('href')
            self.text_target().append('[')
        elif tag == 'br':
            self.text_target().append('\n')
        elif tag == 'strong':
            self.text_target().append('**')

    def handle_endtag(self, tag):
        if tag == 'a':
            self.text_target().append('](' + (self.anchor or '') + ')')
            self.anchor = None
        elif tag == 'strong':
            self.text_target().append('**')
        elif tag in ('th', 'td'):
            if self.row is not None and self.cell is not None:
                self.row.append(''.join(self.cell).strip())
            self.cell = None
            self.cell_tag = None
        elif tag == 'tr':
            if self.table is not None and self.row:
                self.table.append(self.row)
            self.row = None
        elif tag == 'table':
            self.flush_block()
            if self.table:
                self.blocks.append(self.table_to_markdown(self.table))
            self.table = None
        elif tag == 'li':
            self.flush_block()
        elif tag in ('p', 'h2', 'h3'):
            self.flush_block()
        elif tag in ('ul', 'ol'):
            self.flush_block()
            self.list_tag = None

    def handle_data(self, data):
        self.text_target().append(data)

    @staticmethod
    def table_to_markdown(rows):
        clean = []
        width = max(len(row) for row in rows)
        for row in rows:
            clean.append([cell.replace('|', '\\|').replace('\n', ' ') for cell in row] + [''] * (width - len(row)))
        lines = ['| ' + ' | '.join(clean[0]) + ' |']
        lines.append('| ' + ' | '.join(['---'] * width) + ' |')
        lines.extend('| ' + ' | '.join(row) + ' |' for row in clean[1:])
        return '\n'.join(lines)


class VisibleTextParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.parts = []

    def handle_data(self, data):
        self.parts.append(data)


def body_to_markdown(body_html):
    parser = MarkdownBodyParser()
    parser.feed(body_html)
    return '\n\n'.join(parser.blocks).strip()


def visible_body_text(body_html):
    parser = VisibleTextParser()
    parser.feed(body_html)
    return unescape(''.join(parser.parts))


def make_review_markdown(data, body_md, characters, words):
    lines = [
        f"# {data['reviewTitle']}",
        '',
        'Nutrition Concepts & Controversies 第 17 版書籍連載',
        '文件用途：供人工審閱的完整 SEO 草稿與研究回報，尚未代表文章通過審閱。',
        f"作者：{data['author']}",
        '',
        '## 1. SEO 標題',
        '',
        data['seoTitle'],
        '',
        '## 2. 目標搜尋字詞、相關搜尋字詞與搜尋意圖',
        '',
        '- 目標搜尋字詞：' + '、'.join(data['targetTerms']),
        '- 相關搜尋字詞：' + '、'.join(data['relatedTerms']),
        '- 搜尋意圖：' + data['searchIntent'],
        '',
        '## 3. 文章摘要與適合搜尋結果顯示的開場',
        '',
        '### 文章摘要',
        '',
        data['summary'],
        '',
        '### 搜尋結果開場',
        '',
        data['opening'],
        '',
        '## 4. 正文',
        '',
        f"## {data['articleTitle']}",
        '',
        '本篇整理書籍：《Nutrition Concepts & Controversies》第 17 版。',
        '本篇章節：Chapter 9，Energy Balance and a Healthy Body（能量平衡與健康身體）。',
        '本章爭議：Controversy 9，The Grip of Eating Disorders（飲食失調的拉力）。',
        '',
        body_md,
        '',
        '## 5. SEO 描述',
        '',
        data['seoDescription'],
        '',
        '## 6. 文章分類、標籤與網址 slug',
        '',
        '分類：' + data['category'],
        '標籤：' + '、'.join(data['tags']),
        '網址 slug：' + data['slug'],
        'canonical：' + data['canonical'],
        '',
        '## 7. 594katchang-source.github.io 站內連結建議',
        '',
        '### Canonical 與站內連結建議',
        '',
        'canonical 建議使用正式文章網址，避免草稿、預覽頁或查詢參數被當成主要版本。站內連結宜放在讀者已經需要延伸資訊的段落，連結文字直接寫出主題。',
        '',
    ]
    for label, url in data['internalLinks']:
        lines.append(f'- [{label}]({url})')
    lines.extend([
        '',
        '## 8. FAQ 題目與結構化資料建議',
        '',
        '### FAQ 題目',
        '',
    ])
    lines.extend(f'- {question}' for question in data['faq'])
    lines.extend([
        '',
        '### FAQPage 建議',
        '',
        data['faqSchema'],
        '',
        '## 9. 文章結構化資料、作者、更新日期與 canonical 建議',
        '',
        '### Article Schema 建議',
        '',
    ])
    lines.extend(f'- {item}' for item in data['articleSchema'])
    lines.extend([
        '',
        '作者：' + data['author'],
        '建議更新日期：' + data['reviewDate'],
        'canonical：' + data['canonical'],
        '',
        '## 10. 來源連結與各來源支持的段落或主張',
        '',
        '### 來源與主張對照',
        '',
        '| 來源 | 連結或檔案 | 支持內容 |',
        '| --- | --- | --- |',
    ])
    lines.extend(f"| {label} | {url.replace('|', '\\|')} | {scope.replace('|', '\\|')} |" for label, url, scope in data['sources'])
    lines.extend([
        '',
        '## 11. 文章字數、原創差異化主張與待確認事項',
        '',
        f'- 正文實際字數：{characters} 字元，空白分隔詞數 {words}。統計範圍從正文開場至 FAQ 結束，不含 SEO 欄位、站內連結、結構化資料與來源對照。',
        '',
        '### 原創差異化主張',
        '',
    ])
    lines.extend(f'- {claim}' for claim in data['originalClaims'])
    lines.extend(['', '### 待確認事項', ''])
    lines.extend(f'- {item}' for item in data['pending'])
    return '\n'.join(lines).rstrip() + '\n'


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--source-json', required=True)
    parser.add_argument('--target-docx', required=True)
    parser.add_argument('--target-md', required=True)
    args = parser.parse_args()

    source_json = Path(args.source_json).resolve()
    data = json.loads(source_json.read_text(encoding='utf-8'))
    body_html = (source_json.parent / data['bodyHtmlFile']).read_text(encoding='utf-8')
    data['bodyHtml'] = body_html
    text = visible_body_text(body_html)
    characters = len(re.sub(r'\s+', '', text))
    words = len(re.findall(r'\S+', text))
    data['wordCount'] = {'characters': characters, 'words': words}

    target_docx = Path(args.target_docx).resolve()
    target_md = Path(args.target_md).resolve()
    target_docx.parent.mkdir(parents=True, exist_ok=True)
    target_md.parent.mkdir(parents=True, exist_ok=True)
    build_doc(data, target_docx)
    target_md.write_text(make_review_markdown(data, body_to_markdown(body_html), characters, words), encoding='utf-8')
    print(f'DOCX: {target_docx}')
    print(f'Markdown: {target_md}')
    print(f'正文字元: {characters}')
    print(f'空白分隔詞數: {words}')


if __name__ == '__main__':
    main()
