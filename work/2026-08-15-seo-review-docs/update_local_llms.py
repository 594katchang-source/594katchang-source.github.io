from pathlib import Path


BASE = Path(__file__).resolve().parents[2]
LLMS = BASE / "llms.txt"
LOC = "https://594katchang-source.github.io/blog/post.html?id=2026-08-17-carbohydrates-food-guide"
LINE = f"- 碳水化合物怎麼吃才穩？從全穀、膳食纖維到添加糖：{LOC}"


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
