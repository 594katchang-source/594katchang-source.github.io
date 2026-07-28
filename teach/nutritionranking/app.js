/**
 * NutriRank - Food Nutrition Ranking & Search System (app.js)
 * Core Controller for Single Page Web Application
 */

// Category Mapping from raw database categories to 6 Major Food Groups + Others
const CATEGORY_MAP = {
  '澱粉類': 'grains',
  '穀物類': 'grains',
  '豆類': 'beans-meat',
  '魚貝類': 'beans-meat',
  '蛋類': 'beans-meat',
  '肉類': 'beans-meat',
  '乳品類': 'dairy',
  '蔬菜類': 'vegetables',
  '菇類': 'vegetables',
  '藻類': 'vegetables',
  '水果類': 'fruits',
  '油脂類': 'fats-nuts',
  '堅果及種子類': 'fats-nuts',
  '加工調理食品及其他類': 'others',
  '調味料及香辛料類': 'others',
  '糕餅點心類': 'others',
  '糖類': 'others',
  '飲料類': 'others'
};

const GROUP_DETAILS = {
  'grains': { name: '全穀雜糧類', icon: '🌾', color: 'grains' },
  'beans-meat': { name: '豆魚蛋肉類', icon: '🥩', color: 'beans-meat' },
  'dairy': { name: '乳品類', icon: '🥛', color: 'dairy' },
  'vegetables': { name: '蔬菜類', icon: '🥦', color: 'vegetables' },
  'fruits': { name: '水果類', icon: '🍎', color: 'fruits' },
  'fats-nuts': { name: '油脂與堅果種子類', icon: '🥜', color: 'fats-nuts' },
  'others': { name: '其他類', icon: '🍬', color: 'others' }
};

function escapeHtml(value = '') {
  return String(value).replace(/[&<>"']/g, (char) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#039;' })[char]);
}

// Complete nutrient registry with Metadata and Dietary Reference Intakes (DRIs)
const NUTRIENTS = {
  // Macronutrients
  calories: { name: '熱量', unit: 'kcal', type: 'macro', dri: 2000, desc: '維持生命與活動所需的能量。攝取過多易累積為體脂肪。' },
  protein: { name: '粗蛋白', unit: 'g', type: 'macro', dri: 60, desc: '建造與修補細胞組織（包含肌肉）的最重要原料。' },
  fat: { name: '粗脂肪', unit: 'g', type: 'macro', dri: 60, desc: '提供長期能量，協助脂溶性維生素吸收，維持細胞結構。' },
  carbs: { name: '總碳水化合物', unit: 'g', type: 'macro', dri: 300, desc: '身體最主要且最快速可用的能量來源。' },
  fiber: { name: '膳食纖維', unit: 'g', type: 'macro', dri: 25, desc: '促進腸道蠕動，增加飽足感，幫助排便，維持腸道健康。' },
  sugar: { name: '糖質總量', unit: 'g', type: 'macro', dri: 50, desc: '游離糖與雙糖的總和。攝取過多易增加肥胖及心血管疾病風險。' },
  water: { name: '水分', unit: 'g', type: 'macro', dri: 2000, desc: '身體主要的溶劑與代謝介質，具調節體溫等關鍵生理功能。' },
  cholesterol: { name: '膽固醇', unit: 'mg', type: 'macro', dri: 300, desc: '合成荷爾蒙與細胞膜的原料。血脂過高者需注意適量控制。' },

  // Minerals
  calcium: { name: '鈣', unit: 'mg', type: 'mineral', dri: 1000, desc: '維持骨骼與牙齒發育的主要礦物質。參與神經傳導與肌肉收縮。' },
  potassium: { name: '鉀', unit: 'mg', type: 'mineral', dri: 3100, desc: '調控細胞內液滲透壓與酸鹼平衡，穩定血壓及心肌生理機能。' },
  sodium: { name: '鈉', unit: 'mg', type: 'mineral', dri: 2000, desc: '維持體液滲透壓，調節血壓。攝取過量容易導致水腫與高血壓。' },
  iron: { name: '鐵', unit: 'mg', type: 'mineral', dri: 15, desc: '合成血紅素及肌紅素的核心成分，負責在人體內運送氧氣。' },
  zinc: { name: '鋅', unit: 'mg', type: 'mineral', dri: 15, desc: '多種酵素與胰島素的成分，有助於維持正常免疫、生長與生殖發育。' },
  magnesium: { name: '鎂', unit: 'mg', type: 'mineral', dri: 390, desc: '協助數百種酵素催化，維持心臟、神經與肌肉的正常功能。' },
  phosphorus: { name: '磷', unit: 'mg', type: 'mineral', dri: 800, desc: '骨骼牙齒的組成成分，也是細胞膜脂雙層與高能磷酸鍵(ATP)的重要原料。' },

  // Vitamins
  vitA: { name: '維生素 A', unit: 'IU', type: 'vitamin', dri: 2000, desc: '增進暗處視覺，維持上皮細胞與黏膜健康，有助於免疫防護。' },
  vitB1: { name: '維生素 B1', unit: 'mg', type: 'vitamin', dri: 1.4, desc: '醣類代謝的關鍵輔酶。維持神經系統與心肌肌肉的正常運作。' },
  vitB2: { name: '維生素 B2', unit: 'mg', type: 'vitamin', dri: 1.6, desc: '協助細胞能量代謝，維持皮膚黏膜健康，保護眼睛。' },
  vitB6: { name: '維生素 B6', unit: 'mg', type: 'vitamin', dri: 1.6, desc: '參與蛋白質與氨基酸的代謝。有助於紅血球生成及神經訊息傳遞。' },
  vitB12: { name: '維生素 B12', unit: 'ug', type: 'vitamin', dri: 2.4, desc: '紅血球形成與維護大腦、神經髓鞘健康的必備微量維生素。' },
  vitC: { name: '維生素 C', unit: 'mg', type: 'vitamin', dri: 100, desc: '抗氧化劑。促進膠原蛋白合成及鐵質吸收，提升人體防禦機制。' },
  vitD: { name: '維生素 D', unit: 'ug', type: 'vitamin', dri: 10, desc: '促進鈣質在小腸的吸收，調節骨質鈣化，穩定血鈣平衡。' },
  vitE: { name: '維生素 E', unit: 'mg', type: 'vitamin', dri: 13, desc: '脂溶性抗氧化劑。保護細胞膜免受自由基攻擊，延緩組織老化。' },
  folate: { name: '葉酸', unit: 'ug', type: 'vitamin', dri: 400, desc: '合成DNA與細胞分裂的關鍵因子。對孕期胎兒神經發育極為重要。' }
};

// Dynamic nutrient discovery: runs at database load time to register all trace nutrients
function discoverAllNutrients() {
  const knownKeys = new Set(Object.keys(NUTRIENTS));

  // Classification patterns
  const aminoPattern = /胺酸|胺基酸|[（(](?:Ala|Arg|Asn|Asp|Cys|Gln|Glu|Gly|His|Ile|Leu|Lys|Met|Phe|Pro|Ser|Thr|Trp|Tyr|Val)[)）]/;
  const fattyPattern = /脂肪酸|飽和脂肪|反式脂肪|油酸|[（(]\d+:\d+[)）]|棕櫚|硬脂|肉豆蔻|芥子|花生油/;
  const vitaminPattern = /維生素|生育酚|胡蘿蔔素|菸鹼素|視網醇|核黃素|硫胺素|菸酸|煙酸/;
  const mineralTracePattern = /銅|錳|硒|碘|氟|鉻|鉬|鈷|硼/;
  const sugarPattern = /糖/;
  // Unit extraction: match trailing (g), (mg), (ug), (IU), (kcal) etc.
  const unitSuffixPattern = /[（(](g|mg|ug|μg|IU|kcal|RE|α-TE|kJ)[)）]\s*$/i;

  // Scan all foods to collect unknown keys
  const discoveredKeys = new Map();
  state.nutritionData.forEach(food => {
    Object.keys(food.nutrients).forEach(key => {
      if (!knownKeys.has(key) && !discoveredKeys.has(key)) {
        discoveredKeys.set(key, true);
      }
    });
  });

  // Classify and register each discovered key into NUTRIENTS
  discoveredKeys.forEach((_, key) => {
    if (NUTRIENTS[key]) return; // already registered

    let type = 'other';
    if (aminoPattern.test(key)) {
      type = 'amino';
    } else if (fattyPattern.test(key)) {
      type = 'fatty';
    } else if (vitaminPattern.test(key)) {
      type = 'vitamin';
    } else if (mineralTracePattern.test(key)) {
      type = 'mineral';
    } else if (sugarPattern.test(key) && !aminoPattern.test(key)) {
      type = 'other'; // sugars go into 'other' column
    }

    // Determine unit
    let unit = 'mg'; // sensible default
    const unitMatch = unitSuffixPattern.exec(key);
    if (unitMatch) {
      unit = unitMatch[1].toLowerCase() === 'μg' ? 'ug' : unitMatch[1];
    } else if (type === 'amino') {
      unit = 'mg'; // amino acids reported in mg/100g
    } else if (key === '飽和脂肪' || key === '反式脂肪') {
      unit = 'g';
    } else if (key === '修正熱量') {
      unit = 'kcal';
    } else if (key === '灰分' || key === '酒精含量') {
      unit = 'g';
    } else if (type === 'fatty') {
      unit = 'mg'; // fatty acid fractions in mg/100g
    }

    NUTRIENTS[key] = {
      name: key,
      unit: unit,
      type: type,
      dri: 0,
      desc: `${key}（資料庫動態載入）`,
      dynamic: true
    };
  });

  console.log(`[NutriRank] Discovered ${discoveredKeys.size} trace nutrients. Total nutrients: ${Object.keys(NUTRIENTS).length}.`);
}

// Global App State
let state = {
  nutritionData: [],
  activeView: 'home',
  activeNutrient: 'potassium', // Default selected nutrient for rankings
  searchQuery: '',
  searchCategory: 'all',
  searchPage: 1,
  pageSize: 24,
  compareList: [], // Maximum of 3 items
  
  // Matrix query state parameters
  matrixCategories: ['grains', 'beans-meat', 'dairy', 'vegetables', 'fruits', 'fats-nuts', 'others'],
  matrixNutrients: ['calories', 'protein', 'fat', 'carbs'],
  matrixSortKey: 'calories',
  matrixSortOrder: 'desc',
  matrixPage: 1,
  matrixPageSize: 25,
  matrixSearch: ''
};

// On Page Load Initialization
document.addEventListener('DOMContentLoaded', () => {
  initEventListeners();
  loadDatabase();
});

// 1. Data Hydration & Loading
function loadDatabase() {
  const loadingOverlay = document.getElementById('loading-overlay');
  const progressBar = document.getElementById('db-load-progress');
  
  // Simulate premium visual progress
  let progress = 0;
  const progressInterval = setInterval(() => {
    progress += 10;
    progressBar.style.width = `${progress}%`;
    
    if (progress >= 100) {
      clearInterval(progressInterval);
      
      // Load data natively from imported JS variable
      if (typeof NUTRITION_DATABASE !== 'undefined') {
        state.nutritionData = NUTRITION_DATABASE;
        
        // Dynamically discover and register all trace nutrients from the database
        discoverAllNutrients();
        
        setTimeout(() => {
          loadingOverlay.style.opacity = 0;
          setTimeout(() => {
            loadingOverlay.style.display = 'none';
          }, 500);
        }, 300);

        // Populate rank sidebar buttons dynamically
        renderRankSidebar();
        
        // Populate and configure dynamic Matrix checkboxes
        initMatrixFilters();
        
        // Initialize view
        handleRouting();
      } else {
        const loaderText = document.getElementById('loader-status-text') || loadingOverlay.querySelector('.loader-text');
        loaderText.innerHTML = `<span style="color:var(--color-danger)">資料庫變數未定義。</span>`;
        progressBar.style.backgroundColor = 'var(--color-danger)';
        progressBar.style.width = '100%';
        // Hide spinner, show server usage hint
        const spinner = document.getElementById('loading-spinner');
        if (spinner) spinner.style.display = 'none';
        const hint = document.getElementById('loader-server-hint');
        if (hint) hint.style.display = 'block';
      }
    }
  }, 30);
}

// 2. Routing and Navigation
function mapCategoryNameToKey(name) {
  if (name.includes('穀') || name.includes('澱粉') || name.includes('grains')) return 'grains';
  if (name.includes('豆') || name.includes('肉') || name.includes('蛋') || name.includes('魚') || name.includes('beans-meat')) return 'beans-meat';
  if (name.includes('乳') || name.includes('奶') || name.includes('dairy')) return 'dairy';
  if (name.includes('蔬') || name.includes('菇') || name.includes('藻') || name.includes('vegetables')) return 'vegetables';
  if (name.includes('果') || name.includes('fruits')) return 'fruits';
  if (name.includes('脂') || name.includes('堅果') || name.includes('種子') || name.includes('fats-nuts')) return 'fats-nuts';
  return 'others';
}

function mapNutrientNameToKey(name) {
  // 1. Direct key match (handles Chinese trace keys like 天門冬胺酸(Asp))
  if (NUTRIENTS[name]) return name;

  // 2. Match on the nutrient name sans unit suffix e.g. "粗蛋白(g)" -> "粗蛋白"
  const cleanName = name.replace(/[（(][^)）]*[)）]\s*$/, '').trim();
  if (NUTRIENTS[cleanName]) return cleanName;

  // 3. Fuzzy match by display name property
  const match = Object.keys(NUTRIENTS).find(k => {
    const nutName = NUTRIENTS[k].name;
    return nutName === cleanName || cleanName.includes(nutName) || nutName.includes(cleanName);
  });
  return match;
}

function handleRouting() {
  const hash = window.location.hash || '#home';
  let view = 'home';

  if (hash.startsWith('#rank')) {
    view = 'rank';
    const query = new URLSearchParams(hash.substring(hash.indexOf('?') + 1));
    const nut = query.get('nutrient');
    if (nut && NUTRIENTS[nut]) {
      state.activeNutrient = nut;
    }
  } else if (hash.startsWith('#search')) {
    view = 'search';
    const query = new URLSearchParams(hash.substring(hash.indexOf('?') + 1));
    const q = query.get('q');
    if (q) {
      state.searchQuery = decodeURIComponent(q);
      const searchInput = document.getElementById('search-keyword-input');
      if (searchInput) searchInput.value = state.searchQuery;
    }
  } else if (hash.startsWith('#compare')) {
    view = 'compare';
  } else if (hash.startsWith('#matrix')) {
    view = 'matrix';
    const query = new URLSearchParams(hash.substring(hash.indexOf('?') + 1));
    const cats = query.get('categories');
    const nuts = query.get('nutrients');
    if (cats) {
      state.matrixCategories = decodeURIComponent(cats).split(',').map(name => mapCategoryNameToKey(name));
    }
    if (nuts) {
      state.matrixNutrients = decodeURIComponent(nuts).split(',').map(name => mapNutrientNameToKey(name)).filter(k => k);
    }
    syncMatrixCheckboxes();
  }

  switchView(view);
}

function navigateTo(hash) {
  window.location.hash = hash;
  handleRouting();
}

function switchView(viewName) {
  state.activeView = viewName;

  // Update navigation highlights
  document.querySelectorAll('.nav-item').forEach(item => {
    item.classList.remove('active');
    if (item.getAttribute('data-view') === viewName) {
      item.classList.add('active');
    }
  });

  // Switch display grids
  document.querySelectorAll('.app-view').forEach(view => {
    view.classList.remove('active-view');
  });

  const targetView = document.getElementById(`view-${viewName}`);
  if (targetView) {
    targetView.classList.add('active-view');
    // Scroll window to top
    window.scrollTo({ top: 0, behavior: 'smooth' });
  }

  // Trigger view-specific rendering
  if (viewName === 'rank') {
    renderRankings();
  } else if (viewName === 'search') {
    renderSearchResults();
  } else if (viewName === 'compare') {
    renderComparison();
  } else if (viewName === 'matrix') {
    renderMatrix();
  }
}

// 3. Event Listeners Setup
function initEventListeners() {
  // Hashchange router listener
  window.addEventListener('hashchange', handleRouting);

  // Logo goes home
  document.getElementById('nav-logo').addEventListener('click', () => {
    navigateTo('#home');
  });

  // Nav Items click handler
  document.querySelectorAll('.nav-item').forEach(item => {
    item.addEventListener('click', (e) => {
      e.preventDefault();
      const view = item.getAttribute('data-view');
      navigateTo(`#${view}`);
    });
  });

  // Theme Toggle
  const themeBtn = document.getElementById('btn-theme-toggle');
  themeBtn.addEventListener('click', () => {
    const body = document.body;
    if (body.classList.contains('light-theme')) {
      body.classList.remove('light-theme');
      body.classList.add('dark-theme');
      themeBtn.querySelector('.theme-icon').textContent = '☀️';
    } else {
      body.classList.remove('dark-theme');
      body.classList.add('light-theme');
      themeBtn.querySelector('.theme-icon').textContent = '🌙';
    }
  });

  // Home Screen Preset Links Handler
  document.querySelectorAll('.preset-links a').forEach(link => {
    link.addEventListener('click', (e) => {
      e.preventDefault();
      const nutrient = link.getAttribute('data-nutrient');
      navigateTo(`#rank?nutrient=${nutrient}`);
    });
  });

  // Home Screen Search Trigger
  const homeSearchInput = document.getElementById('home-search-input');
  const homeSearchBtn = document.getElementById('home-search-btn');

  const executeHomeSearch = () => {
    const query = homeSearchInput.value.trim();
    if (query) {
      navigateTo(`#search?q=${encodeURIComponent(query)}`);
    } else {
      navigateTo('#search');
    }
  };

  homeSearchBtn.addEventListener('click', executeHomeSearch);
  homeSearchInput.addEventListener('keypress', (e) => {
    if (e.key === 'Enter') executeHomeSearch();
  });

  // Search View Input and Buttons
  const searchInput = document.getElementById('search-keyword-input');
  const searchBtn = document.getElementById('search-btn');
  const clearBtn = document.getElementById('search-clear-btn');

  const executeSearch = () => {
    state.searchQuery = searchInput.value.trim();
    state.searchPage = 1;
    renderSearchResults();
    
    // Toggle clear button
    clearBtn.style.display = state.searchQuery ? 'block' : 'none';
  };

  searchBtn.addEventListener('click', executeSearch);
  searchInput.addEventListener('keypress', (e) => {
    if (e.key === 'Enter') executeSearch();
  });

  // Debounced real-time keystroke searching
  let searchDebounceTimer;
  searchInput.addEventListener('input', () => {
    clearBtn.style.display = searchInput.value ? 'block' : 'none';
    clearTimeout(searchDebounceTimer);
    searchDebounceTimer = setTimeout(() => {
      state.searchQuery = searchInput.value.trim();
      state.searchPage = 1;
      renderSearchResults();
    }, 250);
  });

  clearBtn.addEventListener('click', () => {
    searchInput.value = '';
    clearBtn.style.display = 'none';
    state.searchQuery = '';
    state.searchPage = 1;
    searchInput.focus();
    renderSearchResults();
  });

  // Category Filter Chips
  document.getElementById('search-category-chips').addEventListener('click', (e) => {
    const chip = e.target.closest('.chip');
    if (!chip) return;

    // Toggle active state
    document.querySelectorAll('#search-category-chips .chip').forEach(c => c.classList.remove('active'));
    chip.classList.add('active');

    state.searchCategory = chip.getAttribute('data-category');
    state.searchPage = 1;
    renderSearchResults();
  });

  // Pagination buttons
  document.getElementById('pag-prev').addEventListener('click', () => {
    if (state.searchPage > 1) {
      state.searchPage--;
      renderSearchResults();
      window.scrollTo({ top: document.querySelector('.search-controls-card').offsetTop - 20, behavior: 'smooth' });
    }
  });

  document.getElementById('pag-next').addEventListener('click', () => {
    const totalResults = getFilteredSearchData().length;
    const maxPage = Math.ceil(totalResults / state.pageSize);
    if (state.searchPage < maxPage) {
      state.searchPage++;
      renderSearchResults();
      window.scrollTo({ top: document.querySelector('.search-controls-card').offsetTop - 20, behavior: 'smooth' });
    }
  });

  // Food detail modal events
  const detailModal = document.getElementById('detail-modal');
  document.getElementById('btn-modal-close').addEventListener('click', () => {
    detailModal.style.display = 'none';
  });

  detailModal.addEventListener('click', (e) => {
    if (e.target === detailModal) {
      detailModal.style.display = 'none';
    }
  });

  // Modal Compare Action button
  document.getElementById('btn-modal-add-compare').addEventListener('click', (e) => {
    const foodId = e.target.getAttribute('data-food-id');
    toggleCompareItem(foodId);
    
    // Update button visual instantly in the modal
    const isAdded = state.compareList.some(item => item.id === foodId);
    updateModalCompareButton(isAdded);
  });

  // Compare View Buttons
  document.getElementById('btn-go-search-compare').addEventListener('click', () => {
    navigateTo('#search');
  });

  document.getElementById('btn-clear-compare').addEventListener('click', () => {
    state.compareList = [];
    updateCompareBadge();
    renderComparison();
    // Synchronize cards inside active search views
    if (state.activeView === 'search') {
      renderSearchResults();
    }
  });
}

// 4. Rankings View Component Generation
function renderRankSidebar() {
  const containerMacro = document.getElementById('rank-btns-macro');
  const containerMineral = document.getElementById('rank-btns-mineral');
  const containerVitamin = document.getElementById('rank-btns-vitamin');

  containerMacro.innerHTML = '';
  containerMineral.innerHTML = '';
  containerVitamin.innerHTML = '';

  Object.entries(NUTRIENTS).forEach(([key, meta]) => {
    const btn = document.createElement('button');
    btn.className = 'sidebar-btn';
    btn.setAttribute('data-nutrient', key);
    btn.innerHTML = `
      <span>${escapeHtml(meta.name)}</span>
      <span class="sidebar-btn-val">${key.charAt(0).toUpperCase() + key.slice(1)}</span>
    `;

    btn.addEventListener('click', () => {
      navigateTo(`#rank?nutrient=${key}`);
    });

    if (meta.type === 'macro') {
      containerMacro.appendChild(btn);
    } else if (meta.type === 'mineral') {
      containerMineral.appendChild(btn);
    } else if (meta.type === 'vitamin') {
      containerVitamin.appendChild(btn);
    }
  });
}

function renderRankings() {
  const activeKey = state.activeNutrient;
  const meta = NUTRIENTS[activeKey];
  if (!meta) return;

  // 1. Highlight sidebar button
  document.querySelectorAll('.sidebar-btn').forEach(btn => {
    btn.classList.remove('active', 'active-macro', 'active-mineral', 'active-vitamin');
    if (btn.getAttribute('data-nutrient') === activeKey) {
      btn.classList.add('active');
      btn.classList.add(`active-${meta.type}`);
    }
  });

  // 2. Set Active Nutrient Details header
  document.getElementById('active-nutrient-name').textContent = `${meta.name} (每 100g 含量排行)`;
  document.getElementById('active-nutrient-unit').textContent = `單位: ${meta.unit}`;
  document.getElementById('active-nutrient-desc').textContent = meta.desc;

  // 3. Segment food into 7 Major Group lists
  const groupedData = {
    grains: [],
    'beans-meat': [],
    dairy: [],
    vegetables: [],
    fruits: [],
    'fats-nuts': [],
    others: []
  };

  // Group and filter items containing this nutrient
  state.nutritionData.forEach(food => {
    const val = food.nutrients[activeKey];
    if (val !== undefined && val > 0) {
      const mappedCategory = CATEGORY_MAP[food.category] || 'others';
      groupedData[mappedCategory].push({
        id: food.id,
        name: food.name,
        category: food.category,
        value: val
      });
    }
  });

  // Sort each group descending
  Object.keys(groupedData).forEach(key => {
    groupedData[key].sort((a, b) => b.value - a.value);
  });

  // Calculate maximum value across ALL groups to establish a visually sound standardized progress bar
  let maxTotalValue = 0;
  Object.values(groupedData).forEach(list => {
    if (list.length > 0 && list[0].value > maxTotalValue) {
      maxTotalValue = list[0].value;
    }
  });

  // If no database items contain this, set safe scale
  if (maxTotalValue === 0) maxTotalValue = 1;

  // 4. Render the 7 Columns
  const gridContainer = document.getElementById('groups-rank-container');
  gridContainer.innerHTML = '';

  const columnsOrder = ['grains', 'beans-meat', 'dairy', 'vegetables', 'fruits', 'fats-nuts', 'others'];

  columnsOrder.forEach(key => {
    const groupMeta = GROUP_DETAILS[key];
    const foodsList = groupedData[key];

    const col = document.createElement('div');
    col.className = 'rank-group-column glass-panel';
    
    // Column Header
    const colHeader = document.createElement('div');
    colHeader.className = 'rank-group-header';
    colHeader.innerHTML = `
      <h3>${groupMeta.icon} ${escapeHtml(groupMeta.name)}</h3>
      <span class="rank-group-count">共 ${foodsList.length} 項</span>
    `;
    col.appendChild(colHeader);

    // List container
    const listScroll = document.createElement('div');
    listScroll.className = 'rank-list-scroll';

    if (foodsList.length === 0) {
      const emptyMsg = document.createElement('div');
      emptyMsg.className = 'slot-empty-text';
      emptyMsg.style.padding = '50px 0';
      emptyMsg.textContent = '此大類食材無相關含量數值';
      listScroll.appendChild(emptyMsg);
    } else {
      foodsList.forEach((food, idx) => {
        const item = document.createElement('div');
        item.className = 'rank-item';
        item.setAttribute('data-food-id', food.id);

        const widthPercent = (food.value / maxTotalValue) * 100;
        
        item.innerHTML = `
          <div class="rank-item-meta">
            <span class="rank-num">${idx + 1}</span>
            <span class="rank-item-name" title="${escapeHtml(food.name)}">${escapeHtml(food.name)}</span>
            <span class="rank-item-val">${escapeHtml(food.value)} <span style="font-size:0.75rem; font-weight:400; color:var(--text-muted)">${escapeHtml(meta.unit)}</span></span>
          </div>
          <div class="rank-item-bar-container">
            <div class="rank-item-bar-fill bar-${meta.type}" style="width: ${widthPercent}%"></div>
          </div>
        `;

        // Click to open Nutrition Facts detailed card modal
        item.addEventListener('click', () => {
          openFoodDetail(food.id);
        });

        listScroll.appendChild(item);
      });
    }

    col.appendChild(listScroll);
    gridContainer.appendChild(col);
  });
}

// 5. Food Search & Pagination Engine
function getFilteredSearchData() {
  let filtered = state.nutritionData;

  // Apply keyword query
  if (state.searchQuery) {
    const q = state.searchQuery.toLowerCase();
    filtered = filtered.filter(food => 
      food.name.toLowerCase().includes(q) || 
      (food.commonName && food.commonName.toLowerCase().includes(q)) ||
      (food.englishName && food.englishName.toLowerCase().includes(q)) ||
      food.category.toLowerCase().includes(q) ||
      food.id.toLowerCase().includes(q)
    );
  }

  // Apply major food group category filter
  if (state.searchCategory !== 'all') {
    filtered = filtered.filter(food => {
      const mappedGroup = CATEGORY_MAP[food.category] || 'others';
      return mappedGroup === state.searchCategory;
    });
  }

  return filtered;
}

function renderSearchResults() {
  const container = document.getElementById('search-results-container');
  const statsText = document.getElementById('search-stats-text');
  const pagination = document.getElementById('pagination-controls');

  const filtered = getFilteredSearchData();
  const totalCount = filtered.length;

  if (totalCount === 0) {
    container.innerHTML = '';
    statsText.innerHTML = `❌ 沒有找到任何符合「<strong>${escapeHtml(state.searchQuery)}</strong>」的食材資訊，請嘗試更換關鍵字。`;
    pagination.style.display = 'none';
    return;
  }

  // Statistics sentence
  if (state.searchQuery || state.searchCategory !== 'all') {
    statsText.innerHTML = `🔍 搜尋完成，共篩選出 <strong>${totalCount}</strong> 項食材（點擊可查看精美包裝營養標示與對比）：`;
  } else {
    statsText.textContent = `📋 台灣官方資料庫中收錄 2,181 項完整食品成分，以下為列表預覽（點擊卡片看詳細）：`;
  }

  // Compute pagination coordinates
  const maxPage = Math.ceil(totalCount / state.pageSize);
  if (state.searchPage > maxPage) state.searchPage = maxPage;
  if (state.searchPage < 1) state.searchPage = 1;

  const startIndex = (state.searchPage - 1) * state.pageSize;
  const endIndex = Math.min(startIndex + state.pageSize, totalCount);
  const paginatedList = filtered.slice(startIndex, endIndex);

  // Render search cards
  container.innerHTML = '';
  paginatedList.forEach(food => {
    const isAdded = state.compareList.some(item => item.id === food.id);
    const card = document.createElement('div');
    card.className = 'food-card glass-panel';
    card.setAttribute('data-food-id', food.id);

    // Dynamic color tags for card headers
    const mappedKey = CATEGORY_MAP[food.category] || 'others';
    const grpDetails = GROUP_DETAILS[mappedKey];

    card.innerHTML = `
      <div class="card-header-row">
        <h3 class="food-name" title="${escapeHtml(food.name)}">${escapeHtml(food.name)}</h3>
        <span class="category-tag" style="border: 1px solid var(--color-${grpDetails.color}); color: var(--color-${grpDetails.color}); background: var(--color-${grpDetails.color}-light)">${escapeHtml(food.category)}</span>
      </div>
      ${food.commonName ? `<div class="card-common-name">俗名：${escapeHtml(food.commonName)}${food.englishName ? ' / ' + escapeHtml(food.englishName) : ''}</div>` : (food.englishName ? `<div class="card-common-name">${escapeHtml(food.englishName)}</div>` : '')}
      <div class="card-nutrients-preview">
        <div class="preview-item">
          <span class="preview-val">${food.nutrients.calories || 0}</span>
          <span>大卡 (kcal)</span>
        </div>
        <div class="preview-item">
          <span class="preview-val">${food.nutrients.protein || 0}</span>
          <span>蛋白 (g)</span>
        </div>
        <div class="preview-item">
          <span class="preview-val">${food.nutrients.fat || 0}</span>
          <span>脂肪 (g)</span>
        </div>
      </div>
      <div class="card-actions">
        <span class="card-id-text">整合編號: ${escapeHtml(food.id)}</span>
        <button class="btn-card-compare ${isAdded ? 'added' : ''}" data-food-id="${escapeHtml(food.id)}">
          ${isAdded ? '移除對比' : '加入對比'}
        </button>
      </div>
    `;

    // Clicking card background opens details facts modal
    card.addEventListener('click', (e) => {
      // Avoid opening modal if they clicked the compare button
      if (e.target.closest('.btn-card-compare')) return;
      openFoodDetail(food.id);
    });

    // Handle adding directly from the search result card
    card.querySelector('.btn-card-compare').addEventListener('click', (e) => {
      e.stopPropagation();
      toggleCompareItem(food.id);
      renderSearchResults(); // update cards states
    });

    container.appendChild(card);
  });

  // Setup Pagination Bar Display
  if (maxPage > 1) {
    pagination.style.display = 'flex';
    document.getElementById('pag-info').textContent = `第 ${state.searchPage} / ${maxPage} 頁 (共 ${totalCount} 項)`;
    document.getElementById('pag-prev').disabled = (state.searchPage === 1);
    document.getElementById('pag-next').disabled = (state.searchPage === maxPage);
  } else {
    pagination.style.display = 'none';
  }
}

// 6. Food Compare Management Dashboard
function toggleCompareItem(foodId) {
  const food = state.nutritionData.find(item => item.id === foodId);
  if (!food) return;

  const existingIndex = state.compareList.findIndex(item => item.id === foodId);
  if (existingIndex > -1) {
    // Remove if already selected
    state.compareList.splice(existingIndex, 1);
  } else {
    // Add if under capacity limit
    if (state.compareList.length >= 3) {
      alert('⚠️ 最多僅能加入 3 種食材進行營養比對，請移除舊的食材後再加入。');
      return;
    }
    state.compareList.push(food);
  }

  updateCompareBadge();
}

function updateCompareBadge() {
  const count = state.compareList.length;
  const badge = document.getElementById('compare-count');
  if (count > 0) {
    badge.textContent = count;
    badge.style.display = 'block';
  } else {
    badge.style.display = 'none';
  }
}

function renderComparison() {
  const slotsContainer = document.getElementById('compared-items-container');
  const detailsSection = document.getElementById('compare-details-section');
  const clearBtn = document.getElementById('btn-clear-compare');

  slotsContainer.innerHTML = '';

  // Render 3 comparative card slots
  for (let i = 0; i < 3; i++) {
    const slot = document.createElement('div');
    slot.className = 'comp-slot-card glass-panel';

    if (i < state.compareList.length) {
      const food = state.compareList[i];
      slot.innerHTML = `
        <div class="slot-item-info">
          <span class="slot-item-name">${escapeHtml(food.name)}</span>
          <span class="slot-item-cat">${escapeHtml(food.category)} (ID: ${escapeHtml(food.id)})</span>
        </div>
        <button class="btn-remove-slot" data-food-id="${food.id}">×</button>
      `;

      slot.querySelector('.btn-remove-slot').addEventListener('click', () => {
        toggleCompareItem(food.id);
        renderComparison();
      });
    } else {
      // Empty comparative slot placeholder
      slot.className += ' slot-empty';
      slot.innerHTML = `<div class="slot-empty-text">待加入對比食品 (${i + 1}/3)</div>`;
    }
    slotsContainer.appendChild(slot);
  }

  // Display details comparative sheet if elements exist
  if (state.compareList.length > 0) {
    detailsSection.style.display = 'block';
    clearBtn.style.display = 'block';
    generateComparisonMatrix();
  } else {
    detailsSection.style.display = 'none';
    clearBtn.style.display = 'none';
  }
}

function generateComparisonMatrix() {
  const headerRow = document.getElementById('compare-table-header');
  const tbody = document.getElementById('compare-table-body');

  // Clear existing cells
  headerRow.innerHTML = '<th>營養分析項目 (每 100g 含量)</th>';
  tbody.innerHTML = '';

  // Append Food Names in headers
  state.compareList.forEach(food => {
    const th = document.createElement('th');
    th.style.width = `${60 / state.compareList.length}%`;
    th.innerHTML = `
      <div style="font-weight:700; color:var(--text-primary)">${escapeHtml(food.name)}</div>
      <div style="font-size:0.75rem; color:var(--text-muted); font-weight:400">${escapeHtml(food.category)}</div>
    `;
    headerRow.appendChild(th);
  });

  // Calculate comparisons row-by-row
  Object.entries(NUTRIENTS).forEach(([key, meta]) => {
    const tr = document.createElement('tr');
    tr.innerHTML = `<td style="font-weight:600; color:var(--text-secondary)">${escapeHtml(meta.name)} (${escapeHtml(meta.unit)})</td>`;

    // Extract values for matching compared items
    const values = state.compareList.map(food => food.nutrients[key] || 0);

    // Determine high / low index tags if comparing >= 2 items
    let maxIdx = -1;
    let minIdx = -1;
    if (state.compareList.length >= 2) {
      // Verify values are not completely identical before drawing attention
      const uniqueVals = new Set(values);
      if (uniqueVals.size > 1) {
        const maxVal = Math.max(...values);
        const minVal = Math.min(...values);
        maxIdx = values.indexOf(maxVal);
        minIdx = values.indexOf(minVal);
      }
    }

    // Append cells
    values.forEach((val, index) => {
      const td = document.createElement('td');
      td.style.fontFamily = 'var(--font-heading)';
      td.style.fontWeight = '600';
      
      // Formatting number dynamically
      td.textContent = `${val} ${meta.unit}`;

      if (index === maxIdx) {
        td.className = 'cell-highlight-high';
        td.innerHTML += ` <span style="font-size:0.75rem; font-weight:bold">🏆 最高</span>`;
      } else if (index === minIdx) {
        td.className = 'cell-highlight-low';
        td.innerHTML += ` <span style="font-size:0.75rem">⚠️ 最低</span>`;
      }

      tr.appendChild(td);
    });

    tbody.appendChild(tr);
  });
}

// 7. Nutrition Facts Modal Controller
function openFoodDetail(foodId) {
  const food = state.nutritionData.find(item => item.id === foodId);
  if (!food) return;

  const modal = document.getElementById('detail-modal');

  // Set modal details header
  document.getElementById('modal-food-name').textContent = food.name;
  document.getElementById('modal-food-id-val').textContent = food.id;

  // Show commonName / englishName if available
  const subtitleEl = document.getElementById('modal-food-subtitle');
  if (subtitleEl) {
    const parts = [];
    if (food.commonName) parts.push(`俗名：${food.commonName}`);
    if (food.englishName) parts.push(food.englishName);
    subtitleEl.textContent = parts.join('  |  ');
    subtitleEl.style.display = parts.length > 0 ? 'block' : 'none';
  }
  
  // Set dynamic visual category tags
  const mappedKey = CATEGORY_MAP[food.category] || 'others';
  const grpDetails = GROUP_DETAILS[mappedKey];
  const catTag = document.getElementById('modal-food-category');
  catTag.textContent = `${grpDetails.icon} ${food.category}`;
  catTag.style.background = `var(--color-${grpDetails.color}-light)`;
  catTag.style.color = `var(--color-${grpDetails.color})`;
  catTag.style.border = `1px solid var(--color-${grpDetails.color})`;

  // Helper utility to safely fetch nutrient value
  const getVal = (key) => food.nutrients[key] !== undefined ? food.nutrients[key] : 0;
  const getValOrDash = (key) => food.nutrients[key] !== undefined ? food.nutrients[key] : '--';

  // 1. Set Left side dials
  document.getElementById('dial-calories').textContent = getVal('calories');
  document.getElementById('dial-protein').textContent = getVal('protein');
  document.getElementById('dial-fat').textContent = getVal('fat');
  document.getElementById('dial-carbs').textContent = getVal('carbs');

  // 2. Set Left side secondary list
  document.getElementById('modal-ind-fiber').textContent = `${getVal('fiber')} g`;
  document.getElementById('modal-ind-sugar').textContent = `${getVal('sugar')} g`;
  document.getElementById('modal-ind-cholesterol').textContent = `${getVal('cholesterol')} mg`;
  document.getElementById('modal-ind-water').textContent = `${getVal('water')} g`;

  // 3. Populate Right Side standard Package-Style Label
  document.getElementById('lbl-calories').textContent = getVal('calories');
  document.getElementById('lbl-protein').textContent = getVal('protein');
  document.getElementById('lbl-fat').textContent = getVal('fat');
  document.getElementById('lbl-carbs').textContent = getVal('carbs');
  document.getElementById('lbl-sugar').textContent = getVal('sugar');
  document.getElementById('lbl-fiber').textContent = getVal('fiber');
  document.getElementById('lbl-sodium').textContent = getVal('sodium');

  // Trace micro elements
  document.getElementById('lbl-potassium').textContent = getVal('potassium');
  document.getElementById('lbl-calcium').textContent = getVal('calcium');
  document.getElementById('lbl-magnesium').textContent = getVal('magnesium');
  document.getElementById('lbl-iron').textContent = getVal('iron');
  document.getElementById('lbl-zinc').textContent = getVal('zinc');
  document.getElementById('lbl-phosphorus').textContent = getVal('phosphorus');

  document.getElementById('lbl-vitA').textContent = getValOrDash('vitA');
  document.getElementById('lbl-vitC').textContent = getValOrDash('vitC');
  document.getElementById('lbl-vitD').textContent = getValOrDash('vitD');
  document.getElementById('lbl-vitE').textContent = getValOrDash('vitE');
  
  document.getElementById('lbl-vitB1').textContent = getValOrDash('vitB1');
  document.getElementById('lbl-vitB2').textContent = getValOrDash('vitB2');
  document.getElementById('lbl-vitB6').textContent = getValOrDash('vitB6');
  document.getElementById('lbl-vitB12').textContent = getValOrDash('vitB12');
  document.getElementById('lbl-folate').textContent = getValOrDash('folate');
  document.getElementById('lbl-cholesterol').textContent = getVal('cholesterol');

  // Saturated fat and trans fat (stored as Chinese trace keys)
  const satFatEl = document.getElementById('lbl-saturated-fat');
  const transFatEl = document.getElementById('lbl-trans-fat');
  const satFatVal = food.nutrients['飽和脂肪'];
  const transFatVal = food.nutrients['反式脂肪'];
  if (satFatEl) satFatEl.textContent = satFatVal !== undefined ? satFatVal : '--';
  if (transFatEl) transFatEl.textContent = transFatVal !== undefined ? transFatVal : '--';

  // 4. Render all remaining dynamic nutrients (amino acids, fatty acids, etc.)
  renderDynamicNutrients(food);

  // 5. Modal Compare button updates
  const actionBtn = document.getElementById('btn-modal-add-compare');
  actionBtn.setAttribute('data-food-id', food.id);
  
  const isAdded = state.compareList.some(item => item.id === food.id);
  updateModalCompareButton(isAdded);

  // Render & Scale display
  modal.style.display = 'flex';
}

// Render all dynamic/trace nutrients (amino acids, fatty acids, other) in the modal
function renderDynamicNutrients(food) {
  const container = document.getElementById('modal-dynamic-nutrients');
  if (!container) return;
  container.innerHTML = '';

  // Define which keys are already shown in the static label section
  const staticKeys = new Set([
    'calories', 'protein', 'fat', 'carbs', 'fiber', 'sugar', 'sodium',
    'water', 'cholesterol', 'potassium', 'calcium', 'magnesium', 'iron',
    'zinc', 'phosphorus', 'vitA', 'vitB1', 'vitB2', 'vitB6', 'vitB12',
    'vitC', 'vitD', 'vitE', 'folate', '飽和脂肪', '反式脂肪'
  ]);

  // Collect nutrient groups from this food's data
  const groups = {
    macro: [],    // remaining macros
    mineral: [],  // trace minerals
    vitamin: [],  // additional vitamins
    amino: [],    // amino acids
    fatty: [],    // fatty acids
    other: []     // everything else
  };

  Object.entries(food.nutrients).forEach(([key, val]) => {
    if (staticKeys.has(key)) return;
    if (val === 0 || val === undefined) return;

    const meta = NUTRIENTS[key];
    if (!meta) return;

    const entry = { key, val, meta };
    const t = meta.type;
    if (t === 'amino') groups.amino.push(entry);
    else if (t === 'fatty') groups.fatty.push(entry);
    else if (t === 'mineral') groups.mineral.push(entry);
    else if (t === 'vitamin') groups.vitamin.push(entry);
    else if (t === 'macro') groups.macro.push(entry);
    else groups.other.push(entry);
  });

  const sections = [
    { title: '🧪 其他維生素', entries: groups.vitamin },
    { title: '⛰️ 微量礦物質', entries: groups.mineral },
    { title: '🥑 脂肪酸組成', entries: groups.fatty },
    { title: '🧬 胺基酸組成', entries: groups.amino },
    { title: '🍬 其他成分', entries: [...groups.macro, ...groups.other] },
  ];

  let hasAny = false;
  sections.forEach(section => {
    if (section.entries.length === 0) return;
    hasAny = true;

    const sectionEl = document.createElement('div');
    sectionEl.className = 'dynamic-nutrient-section';

    const titleEl = document.createElement('div');
    titleEl.className = 'dynamic-section-title';
    titleEl.textContent = section.title;
    sectionEl.appendChild(titleEl);

    const grid = document.createElement('div');
    grid.className = 'dynamic-nutrient-grid';

    section.entries.forEach(({ key, val, meta }) => {
      const cell = document.createElement('div');
      cell.className = 'dynamic-nutrient-cell';
      cell.innerHTML = `
        <span class="dn-name">${escapeHtml(meta.name)}</span>
        <span class="dn-value">${escapeHtml(val)} <span class="dn-unit">${escapeHtml(meta.unit)}</span></span>
      `;
      grid.appendChild(cell);
    });

    sectionEl.appendChild(grid);
    container.appendChild(sectionEl);
  });

  container.style.display = hasAny ? 'block' : 'none';
}

function updateModalCompareButton(isAdded) {
  const btn = document.getElementById('btn-modal-add-compare');
  if (isAdded) {
    btn.textContent = '移除對比名單';
    btn.style.background = 'var(--color-danger)';
  } else {
    btn.textContent = '加入食品對比';
    btn.style.background = 'var(--accent-gradient)';
  }
}

// 6. Interactive Cross-Query Nutrition Matrix (進階交叉查詢)
function initMatrixFilters() {
  const catContainer = document.getElementById('matrix-categories-container');
  if (!catContainer) return; // Guard if elements not present yet
  
  catContainer.innerHTML = '';
  Object.keys(GROUP_DETAILS).forEach(key => {
    const detail = GROUP_DETAILS[key];
    const label = document.createElement('label');
    label.className = `matrix-cb-label ${state.matrixCategories.includes(key) ? 'checked' : ''}`;
    label.innerHTML = `
      <input type="checkbox" value="${key}" ${state.matrixCategories.includes(key) ? 'checked' : ''}>
      <span>${detail.icon} ${detail.name}</span>
    `;
    
    const cb = label.querySelector('input');
    cb.addEventListener('change', () => {
      if (cb.checked) {
        if (!state.matrixCategories.includes(key)) state.matrixCategories.push(key);
        label.classList.add('checked');
      } else {
        state.matrixCategories = state.matrixCategories.filter(k => k !== key);
        label.classList.remove('checked');
      }
      state.matrixPage = 1;
      updateMatrixURL();
      renderMatrix();
    });
    
    catContainer.appendChild(label);
  });
  
  const macroContainer = document.getElementById('matrix-nutrients-macro');
  const minContainer = document.getElementById('matrix-nutrients-mineral');
  const vitContainer = document.getElementById('matrix-nutrients-vitamin');
  
  macroContainer.innerHTML = '';
  minContainer.innerHTML = '';
  vitContainer.innerHTML = '';
  
  Object.keys(NUTRIENTS).forEach(key => {
    const detail = NUTRIENTS[key];
    const label = document.createElement('label');
    label.className = `matrix-cb-label ${state.matrixNutrients.includes(key) ? 'checked' : ''}`;
    label.innerHTML = `
      <input type="checkbox" value="${key}" ${state.matrixNutrients.includes(key) ? 'checked' : ''}>
      <span>${detail.name}</span>
    `;
    
    const cb = label.querySelector('input');
    cb.addEventListener('change', () => {
      if (cb.checked) {
        if (!state.matrixNutrients.includes(key)) state.matrixNutrients.push(key);
        label.classList.add('checked');
      } else {
        state.matrixNutrients = state.matrixNutrients.filter(k => k !== key);
        label.classList.remove('checked');
      }
      state.matrixPage = 1;
      updateMatrixURL();
      renderMatrix();
    });
    
    if (detail.type === 'macro') {
      macroContainer.appendChild(label);
    } else if (detail.type === 'mineral') {
      minContainer.appendChild(label);
    } else if (detail.type === 'vitamin') {
      vitContainer.appendChild(label);
    }
    // Dynamic types are handled below
  });

  // Populate the 3 dynamic columns: amino acids, fatty acids, and others
  const aminoContainer = document.getElementById('matrix-nutrients-amino');
  const fattyContainer = document.getElementById('matrix-nutrients-fatty');
  const otherContainer = document.getElementById('matrix-nutrients-other');

  if (aminoContainer) aminoContainer.innerHTML = '';
  if (fattyContainer) fattyContainer.innerHTML = '';
  if (otherContainer) otherContainer.innerHTML = '';

  // Sort dynamically discovered nutrients alphabetically for each group
  const dynamicNutrients = Object.entries(NUTRIENTS)
    .filter(([, meta]) => meta.dynamic)
    .sort(([keyA], [keyB]) => keyA.localeCompare(keyB, 'zh-Hant-TW'));

  dynamicNutrients.forEach(([key, detail]) => {
    let targetContainer = null;
    if (detail.type === 'amino') targetContainer = aminoContainer;
    else if (detail.type === 'fatty') targetContainer = fattyContainer;
    else targetContainer = otherContainer; // sugar, other

    if (!targetContainer) return;

    const label = document.createElement('label');
    label.className = `matrix-cb-label ${state.matrixNutrients.includes(key) ? 'checked' : ''}`;
    label.innerHTML = `
      <input type="checkbox" value="${key}" ${state.matrixNutrients.includes(key) ? 'checked' : ''}>
      <span>${detail.name}</span>
    `;

    const cb = label.querySelector('input');
    cb.addEventListener('change', () => {
      if (cb.checked) {
        if (!state.matrixNutrients.includes(key)) state.matrixNutrients.push(key);
        label.classList.add('checked');
      } else {
        state.matrixNutrients = state.matrixNutrients.filter(k => k !== key);
        label.classList.remove('checked');
      }
      state.matrixPage = 1;
      updateMatrixURL();
      renderMatrix();
    });

    targetContainer.appendChild(label);
  });
  
  // Bind actions
  document.getElementById('btn-matrix-cat-all').addEventListener('click', () => {
    state.matrixCategories = Object.keys(GROUP_DETAILS);
    syncMatrixCheckboxes();
    state.matrixPage = 1;
    updateMatrixURL();
    renderMatrix();
  });
  
  document.getElementById('btn-matrix-cat-none').addEventListener('click', () => {
    state.matrixCategories = [];
    syncMatrixCheckboxes();
    state.matrixPage = 1;
    updateMatrixURL();
    renderMatrix();
  });
  
  document.getElementById('btn-matrix-nut-all').addEventListener('click', () => {
    state.matrixNutrients = Object.keys(NUTRIENTS);
    syncMatrixCheckboxes();
    state.matrixPage = 1;
    updateMatrixURL();
    renderMatrix();
  });
  
  document.getElementById('btn-matrix-nut-none').addEventListener('click', () => {
    state.matrixNutrients = [];
    syncMatrixCheckboxes();
    state.matrixPage = 1;
    updateMatrixURL();
    renderMatrix();
  });
  
  document.getElementById('btn-matrix-nut-presets-macro').addEventListener('click', () => {
    state.matrixNutrients = Object.keys(NUTRIENTS).filter(k => NUTRIENTS[k].type === 'macro');
    syncMatrixCheckboxes();
    state.matrixPage = 1;
    updateMatrixURL();
    renderMatrix();
  });
  
  document.getElementById('btn-matrix-nut-presets-min').addEventListener('click', () => {
    state.matrixNutrients = Object.keys(NUTRIENTS).filter(k => NUTRIENTS[k].type === 'mineral');
    syncMatrixCheckboxes();
    state.matrixPage = 1;
    updateMatrixURL();
    renderMatrix();
  });
  
  document.getElementById('btn-matrix-nut-presets-vit').addEventListener('click', () => {
    state.matrixNutrients = Object.keys(NUTRIENTS).filter(k => NUTRIENTS[k].type === 'vitamin');
    syncMatrixCheckboxes();
    state.matrixPage = 1;
    updateMatrixURL();
    renderMatrix();
  });

  document.getElementById('btn-matrix-nut-presets-amino').addEventListener('click', () => {
    state.matrixNutrients = Object.keys(NUTRIENTS).filter(k => NUTRIENTS[k].type === 'amino');
    syncMatrixCheckboxes();
    state.matrixPage = 1;
    updateMatrixURL();
    renderMatrix();
  });

  document.getElementById('btn-matrix-nut-presets-fatty').addEventListener('click', () => {
    state.matrixNutrients = Object.keys(NUTRIENTS).filter(k => NUTRIENTS[k].type === 'fatty');
    syncMatrixCheckboxes();
    state.matrixPage = 1;
    updateMatrixURL();
    renderMatrix();
  });

  document.getElementById('btn-matrix-nut-presets-sugar').addEventListener('click', () => {
    // Sugar/other group preset
    state.matrixNutrients = Object.keys(NUTRIENTS).filter(k => {
      const t = NUTRIENTS[k].type;
      return t === 'sugar' || (t === 'other' && NUTRIENTS[k].dynamic);
    });
    syncMatrixCheckboxes();
    state.matrixPage = 1;
    updateMatrixURL();
    renderMatrix();
  });

  // Matrix Live Search and Export bindings
  const searchInput = document.getElementById('matrix-search-input');
  searchInput.addEventListener('input', (e) => {
    state.matrixSearch = e.target.value.trim();
    state.matrixPage = 1;
    renderMatrix();
  });
  
  document.getElementById('btn-matrix-export').addEventListener('click', () => {
    exportMatrixCSV();
  });
}

function syncMatrixCheckboxes() {
  const catLabels = document.querySelectorAll('#matrix-categories-container label');
  if (catLabels.length === 0) return; // Guard if not built yet
  
  catLabels.forEach(label => {
    const cb = label.querySelector('input');
    const checked = state.matrixCategories.includes(cb.value);
    cb.checked = checked;
    label.classList.toggle('checked', checked);
  });
  
  ['macro', 'mineral', 'vitamin', 'amino', 'fatty', 'other'].forEach(type => {
    document.querySelectorAll(`#matrix-nutrients-${type} label`).forEach(label => {
      const cb = label.querySelector('input');
      const checked = state.matrixNutrients.includes(cb.value);
      cb.checked = checked;
      label.classList.toggle('checked', checked);
    });
  });
}

function updateMatrixURL() {
  const catNames = state.matrixCategories.map(k => GROUP_DETAILS[k]?.name || k).join(',');
  const nutNames = state.matrixNutrients.map(k => {
    const nut = NUTRIENTS[k];
    return nut ? `${nut.name}(${nut.unit})` : k;
  }).join(',');
  
  const hash = `#matrix?categories=${encodeURIComponent(catNames)}&nutrients=${encodeURIComponent(nutNames)}`;
  window.history.replaceState(null, '', hash);
}

function renderMatrix() {
  // 1. Get filtered list of foods based on categories and search query
  const filtered = state.nutritionData.filter(food => {
    // Category check
    const mappedCategory = CATEGORY_MAP[food.category] || 'others';
    if (!state.matrixCategories.includes(mappedCategory)) return false;
    
    // Search keyword check
    if (state.matrixSearch) {
      const ms = state.matrixSearch.toLowerCase();
      return food.name.toLowerCase().includes(ms) ||
             (food.commonName && food.commonName.toLowerCase().includes(ms)) ||
             (food.englishName && food.englishName.toLowerCase().includes(ms));
    }
    
    return true;
  });
  
  const totalCount = filtered.length;
  document.getElementById('matrix-total-count').textContent = `共 ${totalCount} 項食品`;
  
  // 2. Sort the filtered data
  const sortKey = state.matrixSortKey;
  const isDesc = state.matrixSortOrder === 'desc';
  
  filtered.sort((a, b) => {
    let valA, valB;
    if (sortKey === 'name') {
      valA = a.name;
      valB = b.name;
    } else if (sortKey === 'category') {
      valA = a.category;
      valB = b.category;
    } else {
      valA = a.nutrients[sortKey] || 0;
      valB = b.nutrients[sortKey] || 0;
    }
    
    if (typeof valA === 'string') {
      return isDesc ? valB.localeCompare(valA, 'zh-Hant-TW') : valA.localeCompare(valB, 'zh-Hant-TW');
    } else {
      return isDesc ? valB - valA : valA - valB;
    }
  });
  
  // 3. Paginate
  const maxPage = Math.max(1, Math.ceil(totalCount / state.matrixPageSize));
  if (state.matrixPage > maxPage) state.matrixPage = maxPage;
  if (state.matrixPage < 1) state.matrixPage = 1;
  
  const startIndex = (state.matrixPage - 1) * state.matrixPageSize;
  const endIndex = Math.min(startIndex + state.matrixPageSize, totalCount);
  const paginatedList = filtered.slice(startIndex, endIndex);
  
  // 4. Render Table Headers
  const table = document.getElementById('matrix-results-table');
  const thead = table.querySelector('thead');
  const tbody = table.querySelector('tbody');
  
  thead.innerHTML = '';
  tbody.innerHTML = '';
  
  const headerRow = document.createElement('tr');
  
  // Base columns
  const baseCols = [
    { key: 'name', name: '食品名稱', isNum: false },
    { key: 'category', name: '大類', isNum: false }
  ];
  
  // Nutrient columns (with fallback for any key not yet in NUTRIENTS)
  const nutCols = state.matrixNutrients.map(k => {
    const nut = NUTRIENTS[k];
    if (nut) {
      return { key: k, name: `${escapeHtml(nut.name)}<br><span style="font-size:0.75rem; font-weight:400; color:var(--text-muted)">(${escapeHtml(nut.unit)})</span>`, isNum: true };
    }
    return { key: k, name: escapeHtml(k), isNum: true };
  });
  
  const allCols = [...baseCols, ...nutCols];
  
  allCols.forEach(col => {
    const th = document.createElement('th');
    th.innerHTML = col.name;
    if (col.isNum) th.className = 'num-val';
    
    // Sort classes
    if (state.matrixSortKey === col.key) {
      th.classList.add(state.matrixSortOrder === 'desc' ? 'sorted-desc' : 'sorted-asc');
    }
    
    // Header click -> Sort
    th.addEventListener('click', () => {
      if (state.matrixSortKey === col.key) {
        state.matrixSortOrder = state.matrixSortOrder === 'desc' ? 'asc' : 'desc';
      } else {
        state.matrixSortKey = col.key;
        state.matrixSortOrder = 'desc';
      }
      renderMatrix();
    });
    
    headerRow.appendChild(th);
  });
  
  thead.appendChild(headerRow);
  
  // 5. Render Table Rows
  if (paginatedList.length === 0) {
    const row = document.createElement('tr');
    row.innerHTML = `
      <td colspan="${allCols.length}" style="text-align:center; padding:40px; color:var(--text-muted)">
        查無符合篩選條件的食品項目
      </td>
    `;
    tbody.appendChild(row);
  } else {
    paginatedList.forEach(food => {
      const row = document.createElement('tr');
      row.setAttribute('data-food-id', food.id);
      
      // Name cell
      const nameTd = document.createElement('td');
      nameTd.style.fontWeight = '600';
      nameTd.textContent = food.name;
      row.appendChild(nameTd);
      
      // Category cell
      const catTd = document.createElement('td');
      const grpKey = CATEGORY_MAP[food.category] || 'others';
      const grp = GROUP_DETAILS[grpKey];
      catTd.innerHTML = `<span class="category-tag" style="border: 1px solid var(--color-${grp.color}); color: var(--color-${grp.color}); background: var(--color-${grp.color}-light); padding:2px 8px; border-radius:6px; font-size:0.8rem;">${escapeHtml(food.category)}</span>`;
      row.appendChild(catTd);
      
      // Nutrient cells
      state.matrixNutrients.forEach(k => {
        const td = document.createElement('td');
        td.className = 'num-val';
        const val = food.nutrients[k];
        td.textContent = val !== undefined ? val : '--';
        row.appendChild(td);
      });
      
      // Click row -> open modal (avoiding double triggers on buttons if any)
      row.addEventListener('click', (e) => {
        openFoodDetail(food.id);
      });
      
      tbody.appendChild(row);
    });
  }
  
  // 6. Render Pagination Controls
  const pagContainer = document.getElementById('matrix-pagination-container');
  pagContainer.innerHTML = '';
  
  if (totalCount > 0) {
    const prevBtn = document.createElement('button');
    prevBtn.className = 'page-btn';
    prevBtn.textContent = '上一頁';
    prevBtn.disabled = state.matrixPage === 1;
    prevBtn.addEventListener('click', (e) => {
      e.stopPropagation();
      state.matrixPage--;
      renderMatrix();
    });
    
    const info = document.createElement('span');
    info.className = 'page-info';
    info.textContent = `第 ${state.matrixPage} / ${maxPage} 頁 (顯示 ${startIndex + 1} - ${endIndex} 項 / 共 ${totalCount} 項)`;
    
    const nextBtn = document.createElement('button');
    nextBtn.className = 'page-btn';
    nextBtn.textContent = '下一頁';
    nextBtn.disabled = state.matrixPage === maxPage;
    nextBtn.addEventListener('click', (e) => {
      e.stopPropagation();
      state.matrixPage++;
      renderMatrix();
    });
    
    pagContainer.appendChild(prevBtn);
    pagContainer.appendChild(info);
    pagContainer.appendChild(nextBtn);
  }
}

function exportMatrixCSV() {
  const filtered = state.nutritionData.filter(food => {
    const mappedCategory = CATEGORY_MAP[food.category] || 'others';
    if (!state.matrixCategories.includes(mappedCategory)) return false;
    
    if (state.matrixSearch) {
      return food.name.toLowerCase().includes(state.matrixSearch.toLowerCase());
    }
    
    return true;
  });
  
  const sortKey = state.matrixSortKey;
  const isDesc = state.matrixSortOrder === 'desc';
  
  filtered.sort((a, b) => {
    let valA, valB;
    if (sortKey === 'name') {
      valA = a.name;
      valB = b.name;
    } else if (sortKey === 'category') {
      valA = a.category;
      valB = b.category;
    } else {
      valA = a.nutrients[sortKey] || 0;
      valB = b.nutrients[sortKey] || 0;
    }
    
    if (typeof valA === 'string') {
      return isDesc ? valB.localeCompare(valA, 'zh-Hant-TW') : valA.localeCompare(valB, 'zh-Hant-TW');
    } else {
      return isDesc ? valB - valA : valA - valB;
    }
  });
  
  const csvHeaders = ['食品整合ID', '食品名稱', '食品大類'];
  state.matrixNutrients.forEach(k => {
    const nut = NUTRIENTS[k];
    csvHeaders.push(nut ? `${nut.name}(${nut.unit})` : k);
  });
  
  const csvRows = [];
  csvRows.push('\ufeff' + csvHeaders.map(h => `"${h.replace(/"/g, '""')}"`).join(','));
  
  filtered.forEach(food => {
    const row = [
      food.id,
      food.name,
      food.category
    ];
    
    state.matrixNutrients.forEach(k => {
      const val = food.nutrients[k];
      row.push(val !== undefined ? val : '');
    });
    
    csvRows.push(row.map(cell => `"${String(cell).replace(/"/g, '""')}"`).join(','));
  });
  
  const csvContent = csvRows.join('\n');
  const blob = new Blob([csvContent], { type: 'text/csv;charset=utf-8;' });
  const url = URL.createObjectURL(blob);
  
  const link = document.createElement('a');
  link.setAttribute('href', url);
  
  const today = new Date().toISOString().slice(0, 10);
  link.setAttribute('download', `NutriRank_進階營養比較_${today}.csv`);
  link.style.visibility = 'hidden';
  document.body.appendChild(link);
  link.click();
  document.body.removeChild(link);
}
