(function () {
  "use strict";

  const PAGE_SIZE = 100;
  const state = { items: [], query: "", kind: "all", page: 1 };
  const elements = {
    query: document.querySelector("#query"),
    status: document.querySelector("#status"),
    list: document.querySelector("#paper-list"),
    pagination: document.querySelector("#pagination"),
    updatedAt: document.querySelector("#updated-at"),
    totalCount: document.querySelector("#total-count"),
    reviewCount: document.querySelector("#review-count"),
    digestCount: document.querySelector("#digest-count"),
  };

  const SEARCH_GROUPS = [
    ["肥胖", "obesity", "obesity management", "obesity metabolism"],
    ["老化", "衰老", "高齡", "older adults", "aging", "healthy aging"],
    ["衰弱", "frailty"],
    ["肌少症", "sarcopenia", "muscle loss"],
    ["營養", "營養學", "nutrition", "nutritional"],
    ["飲食型態", "飲食模式", "dietary pattern", "diet pattern"],
    ["蛋白質", "protein"],
    ["微量營養素", "micronutrients", "vitamins", "minerals"],
    ["精準營養", "precision nutrition"],
    ["代謝體學", "metabolomics", "metabolome"],
    ["生物標記", "biomarkers", "biomarker"],
    ["草藥", "草本", "herbal medicine", "herbal"],
    ["植物化學物", "植物化合物", "phytochemicals", "phytochemical"],
    ["膳食補充品", "營養補充品", "dietary supplements", "supplements"],
    ["慢性腎病", "慢性腎臟病", "chronic kidney disease", "CKD"],
    ["糖尿病", "diabetes", "type 2 diabetes", "T2DM"],
    ["心血管疾病", "cardiovascular disease", "cardiovascular"],
    ["癌症", "cancer", "oncology"],
  ];

  function escapeHtml(value) {
    return String(value == null ? "" : value)
      .replaceAll("&", "&amp;")
      .replaceAll("<", "&lt;")
      .replaceAll(">", "&gt;")
      .replaceAll('"', "&quot;")
      .replaceAll("'", "&#39;");
  }

  function expandSearchTerms(value) {
    const normalized = String(value || "").trim().toLocaleLowerCase("zh-Hant");
    if (!normalized) return [];

    const terms = new Set([normalized]);
    for (const group of SEARCH_GROUPS) {
      const normalizedGroup = group.map((term) => term.toLocaleLowerCase("zh-Hant"));
      if (normalizedGroup.some((term) => normalized.includes(term))) {
        normalizedGroup.forEach((term) => terms.add(term));
      }
    }
    return [...terms];
  }

  function safeUrl(value) {
    try {
      const url = new URL(String(value || ""), window.location.href);
      return url.protocol === "https:" ? url.toString() : "";
    } catch {
      return "";
    }
  }

  function formatDate(value) {
    if (!value) return "尚未標記日期";
    const date = new Date(value);
    if (Number.isNaN(date.getTime())) return "日期未提供";
    return new Intl.DateTimeFormat("zh-Hant-TW", { dateStyle: "medium" }).format(date);
  }

  function kindLabel(kind) {
    return kind === "digest" ? "全文評讀" : "品質評讀";
  }

  function scopeLabel(scope) {
    return scope === "full_text" ? "全文評讀" : "摘要層級評讀，受全文限制";
  }

  function readingSummaryLabel(item) {
    const noteTitle = String(item.noteTitle || "").trim();
    if (/^(全文評讀|摘要層級評讀|品質評讀)\s*：/.test(noteTitle)) return noteTitle;
    const displayTitle = (noteTitle || item.title || "未命名論文")
      .replace(/\s+(review|digest)$/i, "")
      .replace(/\s+(全文評讀|摘要層級評讀|品質評讀|摘要評讀)$/u, "")
      .trim();
    const label = item.kind === "digest" || item.evidenceScope === "full_text" ? "全文評讀" : "品質評讀";
    return `${label}：${displayTitle}`;
  }

  function itemText(item) {
    return [
      item.title,
      item.authors,
      item.journal,
      item.year,
      item.doi,
      item.abstract,
      item.category,
      Array.isArray(item.tags) ? item.tags.join(" ") : "",
      item.noteTitle,
      item.content,
    ].join(" ").toLocaleLowerCase("zh-Hant");
  }

  function filteredItems() {
    const terms = expandSearchTerms(state.query);
    return state.items.filter((item) => {
      if (state.kind !== "all" && item.kind !== state.kind) return false;
      const searchable = itemText(item);
      return !terms.length || terms.some((term) => searchable.includes(term));
    });
  }

  function link(label, url) {
    const safe = safeUrl(url);
    return safe ? `<a class="paper-link" href="${escapeHtml(safe)}" target="_blank" rel="noopener noreferrer">${label}</a>` : "";
  }

  function renderTags(tags) {
    if (!Array.isArray(tags) || !tags.length) return "";
    return `<div class="paper-tags">${tags.map((tag) => `<span>${escapeHtml(tag)}</span>`).join("")}</div>`;
  }

  function renderCards(cards) {
    if (!Array.isArray(cards) || !cards.length) return "";
    const cardsHtml = cards.map((card, index) => `
      <article class="quiz-card">
        <span class="quiz-number">${index + 1}</span>
        <div>
          <h4>${escapeHtml(card.title || `理解卡 ${index + 1}`)}</h4>
          <p><strong>問題</strong>${escapeHtml(card.question)}</p>
          <details><summary>查看答案</summary><p>${escapeHtml(card.answer)}</p></details>
        </div>
      </article>`).join("");
    return `<details class="paper-section"><summary>自我測驗（${cards.length} 張）</summary><div class="quiz-list">${cardsHtml}</div></details>`;
  }

  function renderItem(item) {
    const tags = renderTags(item.tags);
    const fullTextLink = link("合法全文", item.legalFullTextUrl);
    const sourceLink = link("來源頁面", item.sourceUrl);
    const doiLink = item.doi ? `<a class="paper-link" href="https://doi.org/${encodeURIComponent(item.doi)}" target="_blank" rel="noopener noreferrer">DOI</a>` : "";
    return `
      <article class="paper-card">
        <header class="paper-card-head">
          <div>
            <div class="paper-kicker"><span>${escapeHtml(kindLabel(item.kind))}</span><span>${escapeHtml(item.category || "未分類")}</span></div>
            <h2>${escapeHtml(item.title || "未命名論文")}</h2>
          </div>
          <span class="paper-scope">${escapeHtml(scopeLabel(item.evidenceScope))}</span>
        </header>
        <p class="paper-authors">${escapeHtml(item.authors || "作者資料未提供")}</p>
        <div class="paper-meta"><span>${escapeHtml(item.journal || "期刊未提供")}</span><span>${escapeHtml(item.year || "年份未提供")}</span><span>${escapeHtml(item.doi || "DOI 未提供")}</span></div>
        ${item.abstract ? `<details class="paper-section paper-abstract-section"><summary>查看摘要</summary><p class="paper-abstract">${escapeHtml(item.abstract)}</p></details>` : ""}
        ${tags}
        <div class="paper-links">${fullTextLink}${sourceLink}${doiLink}</div>
        <details class="paper-section">
          <summary>${escapeHtml(readingSummaryLabel(item))} <span>${escapeHtml(formatDate(item.completedAt))}</span></summary>
          <div class="paper-note">${escapeHtml(item.content)}</div>
        </details>
        ${renderCards(item.cards)}
      </article>`;
  }

  function renderPagination(totalPages, currentPage, total) {
    if (!total) {
      elements.pagination.innerHTML = "";
      return;
    }
    const firstItem = (currentPage - 1) * PAGE_SIZE + 1;
    const lastItem = Math.min(currentPage * PAGE_SIZE, total);
    const pageButtons = totalPages > 1 ? `
      <div class="page-buttons">
        <button type="button" data-page="${currentPage - 1}" ${currentPage === 1 ? "disabled" : ""}>上一頁</button>
        ${Array.from({ length: totalPages }, (_, index) => index + 1).map((page) => `<button type="button" class="${page === currentPage ? "active" : ""}" data-page="${page}" aria-label="第 ${page} 頁" ${page === currentPage ? 'aria-current="page"' : ""}>${page}</button>`).join("")}
        <button type="button" data-page="${currentPage + 1}" ${currentPage === totalPages ? "disabled" : ""}>下一頁</button>
      </div>` : "";
    elements.pagination.innerHTML = `<div class="page-summary">顯示第 ${firstItem} 至 ${lastItem} 筆，共 ${total} 筆</div>${pageButtons}`;
    elements.pagination.querySelectorAll("button[data-page]").forEach((button) => {
      button.addEventListener("click", () => {
        if (button.disabled) return;
        state.page = Number(button.dataset.page) || 1;
        render();
        window.scrollTo({ top: elements.list.offsetTop - 24, behavior: "smooth" });
      });
    });
  }

  function render() {
    const visible = filteredItems();
    const totalPages = Math.max(1, Math.ceil(visible.length / PAGE_SIZE));
    state.page = Math.min(state.page, totalPages);
    const start = (state.page - 1) * PAGE_SIZE;
    const current = visible.slice(start, start + PAGE_SIZE);
    elements.list.innerHTML = current.length
      ? current.map(renderItem).join("")
      : `<div class="paper-empty"><strong>目前沒有符合條件的公開成果</strong><span>可換一組搜尋詞，或切換成果類型。</span></div>`;
    elements.status.textContent = visible.length ? `顯示第 ${start + 1} 至 ${Math.min(start + PAGE_SIZE, visible.length)} 筆，共 ${visible.length} 筆` : "目前沒有符合條件的公開成果";
    renderPagination(totalPages, state.page, visible.length);
  }

  function updateStats() {
    elements.totalCount.textContent = String(state.items.length);
    elements.reviewCount.textContent = String(state.items.filter((item) => item.kind === "review").length);
    elements.digestCount.textContent = String(state.items.filter((item) => item.kind === "digest").length);
  }

  async function load() {
    try {
      const response = await fetch("./data/papers-public.json", { cache: "no-store" });
      if (!response.ok) throw new Error("data unavailable");
      const data = await response.json();
      if (!data || data.schemaVersion !== 1 || !Array.isArray(data.papers)) throw new Error("invalid data");
      state.items = data.papers.filter((item) => item && ["review", "digest"].includes(item.kind));
      elements.updatedAt.textContent = data.generatedAt ? `更新於 ${formatDate(data.generatedAt)}` : "已載入公開資料";
      updateStats();
      render();
    } catch {
      elements.status.textContent = "公開資料暫時無法讀取，請稍後再試。";
      elements.list.innerHTML = `<div class="paper-empty"><strong>資料載入失敗</strong><span>頁面本身仍可開啟，請稍後重新整理。</span></div>`;
    }
  }

  elements.query.addEventListener("input", (event) => {
    state.query = event.target.value;
    state.page = 1;
    render();
  });

  document.querySelectorAll("[data-kind]").forEach((button) => {
    button.addEventListener("click", () => {
      state.kind = button.dataset.kind;
      state.page = 1;
      document.querySelectorAll("[data-kind]").forEach((item) => item.classList.toggle("active", item === button));
      render();
    });
  });

  load();
}());
