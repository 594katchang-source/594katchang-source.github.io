import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

BASE = Path(__file__).resolve().parents[3]
LLMS = BASE / "llms.txt"
LOC = "https://594katchang-source.github.io/blog/post.html?id=2026-08-20-lipids-fatty-acids-guide"
LINE = f"- 脂質怎麼吃才健康？搞懂飽和脂肪、Omega-3、膽固醇與食用油選擇：{LOC}"


def main():
    content = LLMS.read_text(encoding="utf-8")
    if LOC in content:
        raise SystemExit("target llms entry already exists locally")
    marker = "## 最新文章"
    if marker not in content:
        raise SystemExit("unexpected local llms shape")
    LLMS.write_text(content.replace(marker, marker + "\n" + LINE, 1), encoding="utf-8")
    print(f"updated {LLMS}")


if __name__ == "__main__":
    main()
