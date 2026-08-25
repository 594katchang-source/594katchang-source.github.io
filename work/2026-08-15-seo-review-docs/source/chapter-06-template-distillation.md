# 第六章 Word 版型蒸餾紀錄

## Reference

- retained reference: `D:/@Codex/594katchang-source.github.io-main/work/2026-08-15-seo-review-docs/output/chapter-06-proteins-amino-acids-seo-review.docx`
- SHA-256 at inspection: `686AC61893DE7477A0F6525A0AAD00AA8E9A6E0143B97BDDE20D9C58AC80C31F`
- structural inspection: one section, 132 body paragraphs, 12 tables
- reference render attempt: `D:/@Codex/594katchang-source.github.io-main/work/2026-08-15-seo-review-docs/render/template-ch06`
- visual render status: not completed because the packaged renderer could not find LibreOffice on this host

## Page system

- one portrait section
- page size: 8.50 x 11.00 inches
- margins: left/right/top/bottom 1.00 inch
- no section break in the reference
- header: right aligned `Kat Chang 凱特營養師｜SEO 審閱稿`
- footer: centered `僅供審閱，尚未代表文章通過審閱`

## Typography and paragraph roles

- body uses the retained `Normal` style with Calibri plus East Asian Microsoft JhengHei mapping
- Heading 1: 16 pt, bold, blue `2E74B5`, keep with next
- Heading 2: 13 pt, bold, blue `2E74B5`, keep with next
- Heading 3: 12 pt, bold, navy `1F4D78`, keep with next
- title block: centered, 20 pt, bold, navy
- subtitle: centered, 11 pt, italic, slate gray
- body paragraph: 11 pt, 1.25 line spacing, 6 pt after
- list paragraph: retained `List Bullet` or `List Number` style, compact spacing
- hyperlinks: blue, underlined, external relationship

## Lists and tables

- list markers use real Word list styles, not typed bullet characters
- all tables use retained `Table Grid` style
- table width: 9360 DXA, fixed layout, centered, 120 DXA indent
- table rows carry `w:cantSplit`
- header rows carry `w:tblHeader` and light blue fill `E8EEF5`
- cell margins: top/bottom 80 DXA, start/end 120 DXA
- 3-column reference grid: 3120/3120/3120 DXA
- 4-column reference grid: 2340/2340/2340/2340 DXA
- source-table grid in the reference: 2100/3600/3660 DXA
- Chapter 7 source table has two columns and uses an equal 4680/4680 DXA grid

## Content flow for Chapter 7

1. centered title and book-series subtitle
2. document purpose and author
3. SEO title
4. target terms, related terms, and search intent
5. summary and search-result opening
6.正文, with H2/H3 chapter headings, paragraphs, lists, and judgment tables
7. SEO description
8. category, tags, slug, and canonical
9. internal-link suggestions
10. FAQ and structured-data suggestions
11. author, update date, and canonical suggestions
12. sources and claim-support scope
13. word count, original differentiation, and pending verification items

## Fidelity gates

- reference DOCX remains unchanged
- new DOCX must be created at a different path
- section geometry, header, footer, retained styles, table grid, real lists, and hyperlink relationships must remain source-derived
- structural QA must confirm the complete Chapter 7 source content is present
- visual QA must inspect every rendered page when a working DOCX renderer is available
