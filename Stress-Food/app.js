const goals = {
  antiInflammation: "支持大腦抗發炎",
  serotonin: "蛋白質與色胺酸",
  replacement: "取代手抓零食",
  minerals: "鈣鎂與減少高鈉",
  breakfast: "蛋白質與原型澱粉"
};

const scenarios = [
  {
    code: "A",
    title: "深夜趕工時分",
    text: "你正在為明早的報告挑燈夜戰，很想找點東西撐住腦袋。",
    mission: "組出支持大腦抗發炎、又不讓血糖大起大落的點心或飲品。",
    tags: ["熬夜", "大腦疲勞", "抗發炎"],
    goal: "antiInflammation",
    target: { protein: 1, carb: 0, anti: 3, minerals: 0, convenience: 1 },
    teaching: "深夜趕工時，低糖、好油脂、多酚和適量蛋白質，比只靠甜味或咖啡因更能穩住後半段精神。",
    reflection: "如果你真的想喝一點甜的，可以怎麼搭配，讓它不只是短暫提神？"
  },
  {
    code: "B",
    title: "被責備後心情極度低落",
    text: "午餐時你心累地走進便利商店，想抓一個立刻療癒自己的食物。",
    mission: "組出含蛋白質、色胺酸與適量澱粉的便利商店午餐。",
    tags: ["低落", "便利商店", "血清素"],
    goal: "serotonin",
    target: { protein: 3, carb: 1, anti: 0, minerals: 0, convenience: 2 },
    teaching: "低落時不一定要壓抑想吃療癒食物的衝動，但可以先讓這餐有蛋白質和穩定能量。",
    reflection: "你心情低落時最常買什麼？它缺少哪一個可以讓身體更穩的元素？"
  },
  {
    code: "C",
    title: "週末無聊宅家的焦慮",
    text: "你坐在沙發上想到下週待辦清單，手一直想伸向零食。",
    mission: "組出能保留咀嚼感、份量清楚、又比較穩定情緒的替代零食。",
    tags: ["無聊", "手抓零食", "替代"],
    goal: "replacement",
    target: { protein: 1, carb: 0, anti: 0, minerals: 1, convenience: 2 },
    teaching: "焦慮和無聊常被誤認成餓。好的替代不是完全禁止零食，而是讓份量、咀嚼感和飽足感更可控。",
    reflection: "你最容易一邊滑手機一邊吃什麼？可以怎麼讓份量先被看見？"
  },
  {
    code: "D",
    title: "生理期前的情緒暴躁",
    text: "你感覺浮腫、腰痠，情緒很容易被點燃，也特別想吃重口味。",
    mission: "組出富含鈣鎂鉀、並且減少高鈉負擔的飲食選擇。",
    tags: ["經前", "浮腫", "鈣鎂"],
    goal: "minerals",
    target: { protein: 1, carb: 1, anti: 0, minerals: 3, convenience: 0 },
    teaching: "經前不一定要要求自己吃得完美，可以先增加鈣、鎂、鉀，再留意高鈉是否讓浮腫更明顯。",
    reflection: "經前你最容易偏甜、偏鹹還是偏冰？哪一個最容易先微調？"
  },
  {
    code: "E",
    title: "早晨抗壓早餐",
    text: "想到今天工作很重，你完全不想起床吃早餐，只想空腹喝咖啡。",
    mission: "組出快速完成、有蛋白質與原型澱粉的抗壓早餐。",
    tags: ["早餐", "抗壓", "原型澱粉"],
    goal: "breakfast",
    target: { protein: 2, carb: 2, anti: 0, minerals: 0, convenience: 2 },
    teaching: "抗壓早餐不用完美，最低標準是一份蛋白質、一份原型澱粉，再搭配水或無糖飲品。",
    reflection: "你可以預先準備哪一個兩分鐘內能完成的早餐組合？"
  }
];

const foods = [
  {
    id: "egg",
    name: "茶葉蛋",
    icon: "蛋",
    note: "蛋白質、色胺酸",
    stats: { protein: 2, carb: 0, anti: 0, minerals: 0, convenience: 2, risk: 0 },
    tradeoff: "方便補蛋白質，但單吃缺少澱粉和蔬果。"
  },
  {
    id: "soy",
    name: "無糖豆漿",
    icon: "豆",
    note: "蛋白質、便利",
    stats: { protein: 2, carb: 0, anti: 0, minerals: 1, convenience: 2, risk: 0 },
    tradeoff: "很適合補蛋白質，但如果是正餐通常還需要澱粉或纖維。"
  },
  {
    id: "sweetPotato",
    name: "地瓜",
    icon: "薯",
    note: "原型澱粉、纖維",
    stats: { protein: 0, carb: 2, anti: 0, minerals: 1, convenience: 2, risk: 0 },
    tradeoff: "提供穩定能量，但單吃蛋白質不足。"
  },
  {
    id: "salmonRice",
    name: "鮭魚飯糰",
    icon: "飯",
    note: "澱粉、魚類蛋白",
    stats: { protein: 1, carb: 2, anti: 1, minerals: 0, convenience: 2, risk: 1 },
    tradeoff: "很方便，也有魚類蛋白；要留意調味和鈉含量。"
  },
  {
    id: "chicken",
    name: "舒肥雞胸",
    icon: "雞",
    note: "高蛋白、方便",
    stats: { protein: 3, carb: 0, anti: 0, minerals: 0, convenience: 2, risk: 1 },
    tradeoff: "蛋白質充足，但單吃容易缺澱粉與蔬果。"
  },
  {
    id: "yogurt",
    name: "無糖優格",
    icon: "優",
    note: "蛋白質、鈣",
    stats: { protein: 1, carb: 0, anti: 0, minerals: 2, convenience: 1, risk: 0 },
    tradeoff: "適合當基底，若加水果或燕麥會更完整。"
  },
  {
    id: "berries",
    name: "莓果",
    icon: "莓",
    note: "多酚、抗發炎",
    stats: { protein: 0, carb: 1, anti: 2, minerals: 0, convenience: 0, risk: 0 },
    tradeoff: "抗發炎亮點高，但要搭配蛋白質或脂肪才比較有飽足感。"
  },
  {
    id: "nuts",
    name: "小包堅果",
    icon: "堅",
    note: "好油脂、鎂",
    stats: { protein: 1, carb: 0, anti: 2, minerals: 2, convenience: 2, risk: 0 },
    tradeoff: "很適合補好油脂和礦物質，但份量要先抓好。"
  },
  {
    id: "edamame",
    name: "毛豆",
    icon: "毛",
    note: "蛋白質、咀嚼感",
    stats: { protein: 2, carb: 0, anti: 0, minerals: 1, convenience: 1, risk: 0 },
    tradeoff: "很適合取代一直抓零食的手感，但不是每個場景都買得到。"
  },
  {
    id: "seaweed",
    name: "海苔",
    icon: "海",
    note: "手抓感、低負擔",
    stats: { protein: 0, carb: 0, anti: 0, minerals: 1, convenience: 2, risk: 1 },
    tradeoff: "有手抓感、份量小；部分產品鈉含量較高。"
  },
  {
    id: "banana",
    name: "香蕉",
    icon: "蕉",
    note: "鉀、快速補給",
    stats: { protein: 0, carb: 1, anti: 0, minerals: 2, convenience: 2, risk: 0 },
    tradeoff: "快速方便，適合補鉀；如果當早餐，最好再加蛋白質。"
  },
  {
    id: "oats",
    name: "即食燕麥",
    icon: "麥",
    note: "原型澱粉、鎂",
    stats: { protein: 1, carb: 2, anti: 0, minerals: 2, convenience: 1, risk: 0 },
    tradeoff: "穩定能量不錯；若是調味款，糖量可能上升。"
  },
  {
    id: "tofuGreens",
    name: "豆腐青菜",
    icon: "鈣",
    note: "鈣鎂、正餐",
    stats: { protein: 2, carb: 0, anti: 0, minerals: 3, convenience: 0, risk: 0 },
    tradeoff: "營養密度高，但便利性較低。"
  },
  {
    id: "latte",
    name: "微糖鮮奶茶",
    icon: "茶",
    note: "療癒感、含糖",
    stats: { protein: 1, carb: 1, anti: 0, minerals: 1, convenience: 2, risk: 2 },
    tradeoff: "不是不能喝，但最好搭配蛋白質或減少其他甜食。"
  },
  {
    id: "riceCracker",
    name: "小包米餅",
    icon: "餅",
    note: "脆感、份量明確",
    stats: { protein: 0, carb: 1, anti: 0, minerals: 0, convenience: 2, risk: 1 },
    tradeoff: "比整包零食容易控制份量，但飽足感較弱。"
  },
  {
    id: "cornSoup",
    name: "玉米濃湯",
    icon: "湯",
    note: "溫熱、方便",
    stats: { protein: 0, carb: 1, anti: 0, minerals: 0, convenience: 2, risk: 2 },
    tradeoff: "溫熱有安撫感，但常見鈉含量偏高，蛋白質也不足。"
  },
  {
    id: "blackCoffee",
    name: "黑咖啡",
    icon: "咖",
    note: "提神、無糖",
    stats: { protein: 0, carb: 0, anti: 0, minerals: 0, convenience: 2, risk: 1 },
    tradeoff: "無糖是優點，但空腹或焦慮時可能讓心悸更明顯。"
  },
  {
    id: "salad",
    name: "生菜沙拉",
    icon: "菜",
    note: "纖維、清爽",
    stats: { protein: 0, carb: 0, anti: 1, minerals: 2, convenience: 2, risk: 0 },
    tradeoff: "能補纖維和礦物質，但若沒有蛋白質和澱粉，很快會餓。"
  }
];

const metrics = [
  ["protein", "蛋白質"],
  ["carb", "穩定能量"],
  ["anti", "抗發炎"],
  ["minerals", "礦物質"],
  ["convenience", "可實作"],
  ["risk", "取捨值"]
];

const state = {
  round: 0,
  selectedGoal: null,
  plate: [],
  score: 0,
  submitted: false
};

const els = {
  scenarioCode: document.querySelector("#scenarioCode"),
  scenarioTitle: document.querySelector("#scenarioTitle"),
  scenarioText: document.querySelector("#scenarioText"),
  tagRow: document.querySelector("#tagRow"),
  goalOptions: document.querySelector("#goalOptions"),
  foodGrid: document.querySelector("#foodGrid"),
  pickCounter: document.querySelector("#pickCounter"),
  plateZone: document.querySelector("#plateZone"),
  clearPlateButton: document.querySelector("#clearPlateButton"),
  submitButton: document.querySelector("#submitButton"),
  nextButton: document.querySelector("#nextButton"),
  radarList: document.querySelector("#radarList"),
  roundValue: document.querySelector("#roundValue"),
  scoreValue: document.querySelector("#scoreValue"),
  feedbackTitle: document.querySelector("#feedbackTitle"),
  feedbackText: document.querySelector("#feedbackText"),
  roundLog: document.querySelector("#roundLog"),
  resetButton: document.querySelector("#resetButton"),
  foodTemplate: document.querySelector("#foodTemplate")
};

function currentScenario() {
  return scenarios[state.round];
}

function sumStats() {
  return state.plate.reduce(
    (total, food) => {
      Object.keys(total).forEach((key) => {
        total[key] += food.stats[key] || 0;
      });
      return total;
    },
    { protein: 0, carb: 0, anti: 0, minerals: 0, convenience: 0, risk: 0 }
  );
}

function metricPercent(key, value) {
  if (key === "risk") return Math.min(100, value * 18);
  return Math.min(100, value * 24);
}

function renderScenario() {
  const scenario = currentScenario();
  els.scenarioCode.textContent = `情境 ${scenario.code}`;
  els.scenarioTitle.textContent = scenario.title;
  els.scenarioText.textContent = `${scenario.text} 任務：${scenario.mission}`;
  els.tagRow.replaceChildren(
    ...scenario.tags.map((tag) => {
      const span = document.createElement("span");
      span.className = "tag";
      span.textContent = tag;
      return span;
    })
  );
  els.roundValue.textContent = `${state.round + 1}/${scenarios.length}`;
}

function renderGoals() {
  const scenario = currentScenario();
  els.goalOptions.replaceChildren(
    ...Object.entries(goals).map(([key, label]) => {
      const button = document.createElement("button");
      button.type = "button";
      button.className = "goal-option";
      button.textContent = label;
      button.classList.toggle("active", state.selectedGoal === key);
      button.disabled = state.submitted;
      button.addEventListener("click", () => {
        state.selectedGoal = key;
        renderGoals();
        if (key === scenario.goal) {
          setFeedback("方向很貼近", "現在用食材卡組出能回應這個需求的餐盤。可以有很多種合理搭配。");
        } else {
          setFeedback("這也是一種觀點", "這個判斷可能有部分道理。請再看情境線索，想想哪一個需求最優先。");
        }
        renderPlate();
      });
      return button;
    })
  );
}

function renderFoods() {
  els.foodGrid.replaceChildren(
    ...foods.map((food) => {
      const node = els.foodTemplate.content.firstElementChild.cloneNode(true);
      node.dataset.foodId = food.id;
      node.classList.toggle("selected", state.plate.some((item) => item.id === food.id));
      node.disabled = state.submitted;
      node.querySelector(".food-icon").textContent = food.icon;
      node.querySelector("strong").textContent = food.name;
      node.querySelector("small").textContent = food.note;
      node.addEventListener("click", () => toggleFood(food));
      return node;
    })
  );
}

function renderPlate() {
  els.pickCounter.textContent = `已選 ${state.plate.length}/4`;
  if (!state.plate.length) {
    els.plateZone.innerHTML = "<p>從左邊選 2 到 4 張食材卡。這裡沒有唯一答案，重點是說得出你的搭配理由。</p>";
  } else {
    els.plateZone.replaceChildren(
      ...state.plate.map((food) => {
        const chip = document.createElement("button");
        chip.type = "button";
        chip.className = "plate-chip";
        chip.disabled = state.submitted;
        chip.textContent = `${food.icon} ${food.name}`;
        chip.addEventListener("click", () => toggleFood(food));
        return chip;
      })
    );
  }
  els.submitButton.disabled = state.submitted || !state.selectedGoal || state.plate.length < 2;
  els.clearPlateButton.disabled = state.submitted || state.plate.length === 0;
}

function renderRadar() {
  const stats = sumStats();
  els.radarList.replaceChildren(
    ...metrics.map(([key, label]) => {
      const row = document.createElement("div");
      row.className = key === "risk" ? "radar-row risk" : "radar-row";
      row.innerHTML = `
        <span>${label}</span>
        <div class="bar"><i style="width:${metricPercent(key, stats[key])}%"></i></div>
        <strong>${stats[key]}</strong>
      `;
      return row;
    })
  );
  els.scoreValue.textContent = state.score;
}

function toggleFood(food) {
  if (state.submitted) return;
  const exists = state.plate.some((item) => item.id === food.id);
  if (exists) {
    state.plate = state.plate.filter((item) => item.id !== food.id);
  } else if (state.plate.length < 4) {
    state.plate.push(food);
  } else {
    setFeedback("餐盤已滿", "最多選 4 張食材卡。這個限制是為了練習在真實生活中做簡單、可執行的選擇。");
  }
  renderFoods();
  renderPlate();
  renderRadar();
}

function scorePlate() {
  const scenario = currentScenario();
  const stats = sumStats();
  let points = state.selectedGoal === scenario.goal ? 18 : 10;
  let matched = 0;
  const gaps = [];

  Object.entries(scenario.target).forEach(([key, target]) => {
    if (target === 0) return;
    const value = stats[key];
    if (value >= target) {
      matched += 1;
      points += 14;
    } else if (value > 0) {
      points += 8;
      gaps.push(metrics.find(([metric]) => metric === key)[1]);
    } else {
      gaps.push(metrics.find(([metric]) => metric === key)[1]);
    }
  });

  points += Math.min(stats.convenience, 3) * 4;
  points += state.plate.length >= 2 && state.plate.length <= 3 ? 10 : 5;
  points -= Math.max(0, stats.risk - 2) * 4;

  if (stats.risk > 0 && stats.protein + stats.carb + stats.minerals + stats.anti >= 5) {
    points += 4;
  }

  return {
    points: Math.max(0, Math.min(100, points)),
    stats,
    matched,
    gaps
  };
}

function describePlate(result) {
  const strengths = [];
  const stats = result.stats;
  if (stats.protein >= 2) strengths.push("有蛋白質支撐");
  if (stats.carb >= 2) strengths.push("有穩定能量");
  if (stats.anti >= 2) strengths.push("有抗發炎亮點");
  if (stats.minerals >= 2) strengths.push("有礦物質補強");
  if (stats.convenience >= 2) strengths.push("可實作性高");

  const tradeoffs = state.plate
    .filter((food) => food.stats.risk > 0 || food.tradeoff.includes("但"))
    .slice(0, 2)
    .map((food) => `${food.name}：${food.tradeoff}`);

  const strengthText = strengths.length ? `優點：${strengths.join("、")}。` : "這組選擇有討論空間。";
  const gapText = result.gaps.length ? `可以補強：${[...new Set(result.gaps)].join("、")}。` : "主要需求都有照顧到。";
  const tradeoffText = tradeoffs.length ? `取捨：${tradeoffs.join(" ")}` : "取捨：這組相對單純，下一步可討論是否真的買得到、做得到。";
  return `${strengthText} ${gapText} ${tradeoffText}`;
}

function submitPlate() {
  if (state.submitted || !state.selectedGoal || state.plate.length < 2) return;
  const scenario = currentScenario();
  const result = scorePlate();
  state.submitted = true;
  state.score += result.points;

  const level = result.points >= 78 ? "高適配" : result.points >= 58 ? "可行但可調整" : "需要說明理由";
  setFeedback(
    `${result.points} 分：${level}`,
    `${scenario.teaching} ${describePlate(result)} 反思：${scenario.reflection}`
  );

  addLog(result.points, level);
  renderGoals();
  renderFoods();
  renderPlate();
  renderRadar();
  els.nextButton.disabled = false;
}

function addLog(points, level) {
  const scenario = currentScenario();
  const item = document.createElement("li");
  const names = state.plate.map((food) => food.name).join("、");
  item.textContent = `情境 ${scenario.code}：${names}，${level}，${points} 分。`;
  els.roundLog.append(item);
}

function nextRound() {
  if (state.round === scenarios.length - 1) {
    finishGame();
    return;
  }
  state.round += 1;
  state.selectedGoal = null;
  state.plate = [];
  state.submitted = false;
  els.nextButton.disabled = true;
  setFeedback("先判斷，再組餐", "先看情境線索，再選營養目標。選項不是非黑即白，重點是能說明你的取捨。");
  renderAll();
}

function finishGame() {
  const high = state.score >= 330;
  setFeedback(
    high ? "完成壓力飲食偵探任務" : "完成五個生活情境",
    high
      ? "你已經能從壓力情境推回飲食需求。最後請選一個最常發生在自己身上的情境，寫下兩種可行備案。"
      : "分數不是重點。請回看紀錄，找出哪一關最像自己的飲食慣性，從那一關先做一個小改變。"
  );
  els.nextButton.disabled = true;
  els.submitButton.disabled = true;
}

function setFeedback(title, text) {
  els.feedbackTitle.textContent = title;
  els.feedbackText.textContent = text;
}

function resetGame() {
  state.round = 0;
  state.selectedGoal = null;
  state.plate = [];
  state.score = 0;
  state.submitted = false;
  els.roundLog.replaceChildren();
  els.nextButton.disabled = true;
  setFeedback("先判斷，再組餐", "每一關都不是背標準答案，而是練習在真實生活中做有理由的飲食取捨。");
  renderAll();
}

function renderAll() {
  renderScenario();
  renderGoals();
  renderFoods();
  renderPlate();
  renderRadar();
}

els.clearPlateButton.addEventListener("click", () => {
  if (state.submitted) return;
  state.plate = [];
  renderFoods();
  renderPlate();
  renderRadar();
});
els.submitButton.addEventListener("click", submitPlate);
els.nextButton.addEventListener("click", nextRound);
els.resetButton.addEventListener("click", resetGame);

resetGame();
