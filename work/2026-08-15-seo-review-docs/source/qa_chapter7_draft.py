import re
from pathlib import Path


ROOT = Path(__file__).resolve().parent
DRAFT = ROOT.parent / "output" / "chapter-07-vitamins-seo-review.md"
text = DRAFT.read_text(encoding="utf-8")
body = text.split("## 4. 正文", 1)[1].split("## 5. SEO 描述", 1)[0]
visible = re.sub(r"[`#>*|\[\]()]", "", body)
visible = re.sub(r"https?://\S+", "", visible)
visible = re.sub(r"\s+", "", visible)
blacklist = [
    "再者", "然而", "不過", "值得注意的是", "由此可見", "可以看出", "總之", "總而言之", "總的來說",
    "整體而言", "大體而言", "綜上所述", "綜合來看", "綜觀以上", "換句話說", "換言之", "首先", "其次",
    "再次", "最後", "全面", "全方位", "系統性", "多層次", "多維度", "多角度", "顛覆性", "革命性",
    "劃時代", "前所未有", "意義重大", "具有重要意義", "影響深遠", "不可忽視", "舉足輕重", "令人印象深刻",
    "發人深省", "耐人尋味", "引人入勝", "耳目一新", "極具潛力", "極具前景", "極具發展空間", "不僅",
    "不只", "不是", "而是", "接下來", "我們將探討", "讓我們一起來看看", "這篇文章將帶你了解", "透過上述介紹",
    "相信你已經", "無論你是", "如果你也有同樣的困惑",
]
hits = {word: text.count(word) for word in blacklist if word in text}
print({
    "file": str(DRAFT),
    "body_visible_characters": len(visible),
    "body_requirement_met": len(visible) >= 2000,
    "h2_count": len(re.findall(r"^## ", body, flags=re.M)),
    "h3_count": len(re.findall(r"^### ", body, flags=re.M)),
    "table_count": body.count("|---|"),
    "faq_count": len(re.findall(r"^### .*？", body, flags=re.M)),
    "source_link_count": len(re.findall(r"https?://", text)),
    "blacklist_hits": hits,
})
if len(visible) < 2000 or hits:
    raise SystemExit(1)
