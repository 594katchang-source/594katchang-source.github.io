import { initializeApp } from "https://www.gstatic.com/firebasejs/10.12.5/firebase-app.js";
import { getDatabase, ref, set, update, onValue, get, runTransaction, serverTimestamp } from "https://www.gstatic.com/firebasejs/10.12.5/firebase-database.js";

const DEFAULT_FIREBASE_CONFIG = {
  apiKey: "AIzaSyBFPjEXxNp5-UPqApClA1FaACD4UE6aRT0",
  authDomain: "realtime-database-2fcbb.firebaseapp.com",
  databaseURL: "https://realtime-database-2fcbb-default-rtdb.firebaseio.com",
  projectId: "realtime-database-2fcbb",
  storageBucket: "realtime-database-2fcbb.firebasestorage.app",
  messagingSenderId: "7723390214",
  appId: "1:7723390214:web:a227cd5d88b9f01274fa87"
};

const q = (text, options, answer, explain) => ({ text, options, answer, explain });
const banks = {
  classify: {
    label: "第一模式：食物分類",
    questions: [
      q("地瓜在食物代換表中主要屬於哪一類？", ["蔬菜類", "全穀雜糧類", "水果類", "豆魚蛋肉類"], 1, "地瓜富含澱粉，代換時歸全穀雜糧類。"),
      q("毛豆、黃豆、黑豆與豆腐、豆漿主要屬於哪一類？", ["豆魚蛋肉類", "水果類", "蔬菜類", "油脂堅果類"], 0, "這些是植物性優質蛋白質來源。"),
      q("南瓜代換時主要屬於哪一類？", ["蔬菜類", "全穀雜糧類", "乳品類", "水果類"], 1, "南瓜含澱粉較多。"),
      q("一杯 240 毫升鮮奶主要歸在哪一類？", ["乳品類", "豆魚蛋肉類", "水果類", "油脂堅果類"], 0, "鮮奶、保久乳、無糖優格都屬乳品類。"),
      q("杏仁果、花生、腰果主要歸在哪一類？", ["水果類", "豆魚蛋肉類", "油脂與堅果種子類", "蔬菜類"], 2, "堅果種子含油脂，份量要控制。"),
      q("雞蛋、魚肉、雞肉共同屬於哪一類？", ["乳品類", "豆魚蛋肉類", "全穀雜糧類", "蔬菜類"], 1, "蛋、魚、海鮮、禽肉、畜肉都屬豆魚蛋肉類。"),
      q("紅豆、綠豆在代換概念中較接近哪一類？", ["乳品類", "全穀雜糧類", "豆魚蛋肉類", "油脂堅果類"], 1, "紅豆、綠豆不同於黃豆、黑豆、毛豆。"),
      q("大番茄作為料理時常歸為哪一類？", ["蔬菜類", "水果類", "乳品類", "全穀雜糧類"], 0, "大番茄常作蔬菜類。"),
      q("馬鈴薯應該和哪一類食物互相代換？", ["水果", "乳品", "全穀雜糧", "豆魚蛋肉"], 2, "馬鈴薯富含澱粉。"),
      q("豆干、豆腐、無糖豆漿主要提供什麼？", ["蛋白質", "維生素 C", "單純油脂", "酒精"], 0, "黃豆製品是重要蛋白質來源。")
    ]
  },
  portion: {
    label: "第二模式：我的餐盤份量",
    questions: [
      q("「每天早晚一杯奶」的一杯約是多少？", ["120 毫升", "190 毫升", "240 毫升", "500 毫升"], 2, "我的餐盤一杯乳品約 240 毫升。"),
      q("每餐水果建議大約是多少？", ["一個拳頭大", "一掌心", "一茶匙", "半個餐盤"], 0, "口訣是每餐水果拳頭大。"),
      q("蔬菜份量和水果相比，哪個較符合口訣？", ["菜比水果少一點", "菜比水果多一點", "不用吃菜", "只吃水果"], 1, "口訣是菜比水果多一點。"),
      q("飯和蔬菜的份量關係，哪個最接近？", ["飯跟蔬菜一樣多", "飯比菜多三倍", "完全不吃飯", "只有飯不用菜"], 0, "口訣是飯跟蔬菜一樣多。"),
      q("每餐豆魚蛋肉類大約是多少？", ["一掌心", "一茶匙", "兩大碗", "一整盤"], 0, "口訣是豆魚蛋肉一掌心。"),
      q("堅果種子每餐建議約是多少？", ["一茶匙", "一飯碗", "一拳頭", "半盤"], 0, "口訣是堅果種子一茶匙。"),
      q("切塊水果一份常用哪個方式估量？", ["標準碗八分滿", "一大鍋", "一茶匙", "一片起司"], 0, "切塊水果可用 240 毫升標準碗八分滿估一份。"),
      q("豆魚蛋肉類建議優先選擇哪一組？", ["加工肉品", "豆類、魚海鮮、蛋、禽畜肉", "培根熱狗", "肥肉"], 1, "少加工，優先豆類、魚類與海鮮。"),
      q("蔬菜一份熟菜大約是多少？", ["半碗", "三大碗", "一茶匙", "一杯奶"], 0, "熟蔬菜常以半碗估一份。"),
      q("堅果一天合計大約可以抓哪個概念？", ["約一湯匙", "約十碗", "完全不需要", "越多越好"], 0, "堅果健康但油脂高。")
    ]
  },
  rainbow: {
    label: "第三模式：彩虹食物",
    questions: [
      q("紅色彩虹食物哪一組最適合？", ["小番茄、紅甜椒、西瓜", "白飯、白吐司", "牛奶、起司", "雞蛋、豆腐"], 0, "紅色蔬果常含茄紅素等植化素。"),
      q("哪一個橘黃色食物也常歸全穀雜糧類代換？", ["南瓜", "芭樂", "牛奶", "豆腐"], 0, "南瓜含澱粉，代換時歸全穀雜糧類。"),
      q("深綠色蔬菜哪一組最適合？", ["菠菜、地瓜葉、青江菜", "香蕉、芒果", "鮮奶、優格", "核桃、花生"], 0, "深綠色蔬菜是彩虹飲食重要來源。"),
      q("紫色全穀或蔬果哪一組較適合？", ["紫米、茄子、葡萄", "白飯、白麵條", "雞肉、魚肉", "牛奶、豆漿"], 0, "紫色食物也能進餐盤。"),
      q("想讓一餐更像彩虹，最好的做法是？", ["固定只吃一種顏色", "多選不同顏色", "完全不吃菜", "只喝含糖飲料"], 1, "彩虹飲食強調不同顏色輪流吃。"),
      q("白色或淺色食物中，哪個是蔬菜類？", ["白蘿蔔", "白吐司", "白飯", "奶粉"], 0, "白蘿蔔是蔬菜類。"),
      q("彩虹全穀雜糧哪一組較符合？", ["糙米、紫米、玉米、地瓜", "火腿、熱狗", "起司、鮮奶", "白開水、茶"], 0, "全穀雜糧也可以有顏色變化。"),
      q("為什麼不能只用顏色判斷食物類別？", ["同色食物可能分屬不同類別", "顏色淡一定不健康", "紅色都算水果", "綠色都算蔬菜"], 0, "分類仍要看主要營養特性。"),
      q("黃色水果的例子哪一個較適合？", ["木瓜", "豆腐", "白飯", "雞肉"], 0, "木瓜可作為橘黃色水果例子。"),
      q("綠色食物中，哪一個也是豆魚蛋肉類的豆類代表？", ["毛豆", "白吐司", "葡萄", "起司"], 0, "毛豆是綠色豆類食物，也是植物性蛋白質來源。")
    ]
  }
};

const state = {
  role: "landing",
  room: "",
  uid: localStorage.getItem("nutrition_uid") || crypto.randomUUID(),
  config: null,
  db: null,
  roomData: null,
  selectedCount: 10,
  sound: true
};
localStorage.setItem("nutrition_uid", state.uid);

const el = (id) => document.getElementById(id);
const screens = ["landingScreen", "setupScreen", "hostScreen", "studentScreen"];
const params = new URLSearchParams(location.search);

function show(id) {
  screens.forEach((screen) => el(screen).classList.toggle("active", screen === id));
}

function encodeConfig(config) {
  return btoa(unescape(encodeURIComponent(JSON.stringify(config)))).replaceAll("+", "-").replaceAll("/", "_").replaceAll("=", "");
}

function decodeConfig(value) {
  const padded = value.replaceAll("-", "+").replaceAll("_", "/") + "===".slice((value.length + 3) % 4);
  return JSON.parse(decodeURIComponent(escape(atob(padded))));
}

function loadConfig() {
  const embedded = window.NUTRITION_FIREBASE_CONFIG || DEFAULT_FIREBASE_CONFIG;
  if (params.get("cfg")) return { ...embedded, ...decodeConfig(params.get("cfg")) };
  const saved = localStorage.getItem("nutrition_firebase_config");
  return saved ? { ...embedded, ...JSON.parse(saved) } : embedded;
}

function initFirebase(config) {
  if (state.db) return state.db;
  state.config = config;
  state.db = getDatabase(initializeApp(config));
  return state.db;
}

function roomRef(path = "") {
  return ref(state.db, `rooms/${state.room}${path ? `/${path}` : ""}`);
}

function randomRoomCode() {
  return Math.random().toString(36).slice(2, 6).toUpperCase();
}

function shuffle(items) {
  return [...items].map((item) => ({ item, sort: Math.random() })).sort((a, b) => a.sort - b.sort).map(({ item }) => item);
}

function playTone(kind) {
  if (!state.sound) return;
  const audio = new AudioContext();
  const gain = audio.createGain();
  const osc = audio.createOscillator();
  const freq = { join: 520, buzz: 760, right: 920, wrong: 160, next: 440 }[kind] || 440;
  osc.frequency.value = freq;
  osc.type = kind === "wrong" ? "sawtooth" : "sine";
  gain.gain.setValueAtTime(0.001, audio.currentTime);
  gain.gain.exponentialRampToValueAtTime(0.12, audio.currentTime + 0.02);
  gain.gain.exponentialRampToValueAtTime(0.001, audio.currentTime + 0.22);
  osc.connect(gain).connect(audio.destination);
  osc.start();
  osc.stop(audio.currentTime + 0.24);
}

function renderModeOptions() {
  el("modeSelect").innerHTML = Object.entries(banks).map(([key, bank]) => `<option value="${key}">${bank.label}</option>`).join("");
}

async function createRoom() {
  try {
    const config = loadConfig();
    if (!config) return show("setupScreen");
    el("hostBuzz").textContent = "正在建立場次...";
    initFirebase(config);
    state.room = randomRoomCode();
    const mode = el("modeSelect").value;
    const count = Math.max(1, Math.min(60, Number(el("customCount").value || state.selectedCount)));
    const bank = banks[mode].questions;
    const order = shuffle(bank.map((_, index) => index)).slice(0, Math.min(count, bank.length));
    await set(roomRef(), {
      code: state.room,
      mode,
      requestedCount: count,
      order,
      index: -1,
      status: "lobby",
      scores: { red: 0, blue: 0 },
      buzz: null,
      answer: null,
      createdAt: serverTimestamp()
    });
    listenRoom();
    const joinUrl = `${location.origin}${location.pathname}?room=${state.room}&cfg=${encodeConfig(config)}`;
    el("roomCode").textContent = state.room;
    el("qrCode").src = `https://api.qrserver.com/v1/create-qr-code/?size=240x240&data=${encodeURIComponent(joinUrl)}`;
    el("startRound").disabled = false;
    el("endRoom").disabled = false;
    playTone("join");
  } catch (error) {
    el("hostBuzz").textContent = `建立場次失敗：${error?.message || error}`;
  }
}

async function startRound() {
  await update(roomRef(), { status: "playing", index: 0, buzz: null, answer: null });
  el("nextQuestion").disabled = false;
  playTone("next");
}

async function nextQuestion() {
  const data = state.roomData;
  if (!data) return;
  const next = (data.index ?? -1) + 1;
  if (next >= data.order.length) await update(roomRef(), { status: "ended", buzz: null });
  else {
    await update(roomRef(), { index: next, buzz: null, answer: null, status: "playing" });
    playTone("next");
  }
}

async function endRoom() {
  await update(roomRef(), { status: "ended", buzz: null });
}

async function joinRoom() {
  try {
    const config = loadConfig();
    if (!config) return show("setupScreen");
    initFirebase(config);
    state.room = el("joinCode").value.trim().toUpperCase();
    const name = el("studentName").value.trim() || `學員${Math.floor(Math.random() * 90 + 10)}`;
    el("studentBuzz").textContent = "正在加入場次...";
    const snapshot = await get(roomRef());
    if (!snapshot.exists()) {
      el("studentBuzz").textContent = "找不到這個場次，請確認代碼。";
      return;
    }
    await runTransaction(roomRef("players"), (players) => {
      players = players || {};
      const list = Object.values(players);
      const redCount = list.filter((player) => player.team === "red").length;
      const blueCount = list.filter((player) => player.team === "blue").length;
      const team = redCount === blueCount ? (Math.random() > 0.5 ? "red" : "blue") : redCount < blueCount ? "red" : "blue";
      players[state.uid] = { name, team, joinedAt: Date.now() };
      return players;
    });
    el("joinPanel").classList.add("hidden");
    el("studentGame").classList.remove("hidden");
    listenRoom();
    playTone("join");
  } catch (error) {
    el("studentBuzz").textContent = `加入失敗：${error?.message || error}`;
  }
}

async function buzzMe() {
  const me = state.roomData?.players?.[state.uid];
  if (!me || state.roomData?.buzz || state.roomData?.answer || state.roomData?.status !== "playing") return;
  await runTransaction(roomRef("buzz"), (current) => current || { uid: state.uid, name: me.name, team: me.team, at: Date.now() });
  playTone("buzz");
}

async function answerQuestion(choice) {
  const data = state.roomData;
  const me = data?.players?.[state.uid];
  if (!me || data?.buzz?.uid !== state.uid || data?.answer) return;
  const question = currentQuestion(data);
  const correct = choice === question.answer;
  const otherTeam = me.team === "red" ? "blue" : "red";
  const scores = data.scores || { red: 0, blue: 0 };
  if (correct) scores[me.team] = (scores[me.team] || 0) + 10;
  else scores[otherTeam] = (scores[otherTeam] || 0) + 5;
  await update(roomRef(), { scores, answer: { uid: state.uid, name: me.name, team: me.team, choice, correct, explain: question.explain } });
  playTone(correct ? "right" : "wrong");
}

function currentQuestion(data) {
  if (!data || data.index < 0) return null;
  return banks[data.mode].questions[data.order[data.index]];
}

function listenRoom() {
  onValue(roomRef(), (snapshot) => {
    state.roomData = snapshot.val();
    if (state.role === "host") renderHost();
    if (state.role === "student") renderStudent();
  });
}

function renderHost() {
  const data = state.roomData;
  if (!data) return;
  el("hostRedScore").textContent = data.scores?.red || 0;
  el("hostBlueScore").textContent = data.scores?.blue || 0;
  renderRoster(data.players || {});
  const question = currentQuestion(data);
  el("hostRound").textContent = data.status === "ended" ? "活動結束" : data.index >= 0 ? `第 ${data.index + 1} 題 / ${data.order.length}` : `等待學員加入：${banks[data.mode].label}`;
  el("hostQuestion").textContent = question ? question.text : "學員掃描 QR Code 後，名字會出現在隊伍名單。";
  renderAnswers(el("hostAnswers"), question, data.answer, false);
  el("hostBuzz").textContent = buzzText(data);
  el("startRound").disabled = data.status !== "lobby";
  el("nextQuestion").disabled = data.status !== "playing" || !data.answer;
}

function renderRoster(players) {
  const red = [];
  const blue = [];
  Object.values(players).forEach((player) => (player.team === "red" ? red : blue).push(`<li>${escapeHtml(player.name)}</li>`));
  el("redRoster").innerHTML = red.join("");
  el("blueRoster").innerHTML = blue.join("");
}

function renderStudent() {
  const data = state.roomData;
  const me = data?.players?.[state.uid];
  if (!data || !me) return;
  el("studentTeam").className = `student-team ${me.team}`;
  el("studentTeam").textContent = `${me.name}，你是${me.team === "red" ? "紅隊" : "藍隊"}`;
  el("studentRedScore").textContent = data.scores?.red || 0;
  el("studentBlueScore").textContent = data.scores?.blue || 0;
  const question = currentQuestion(data);
  el("studentRound").textContent = data.status === "ended" ? "活動結束" : data.index >= 0 ? `第 ${data.index + 1} 題 / ${data.order.length}` : "等待講師開始";
  el("studentQuestion").textContent = question ? question.text : "請看講台畫面，等待講師開始。";
  el("buzzMe").disabled = data.status !== "playing" || Boolean(data.buzz) || Boolean(data.answer);
  renderAnswers(el("studentAnswers"), question, data.answer, data.buzz?.uid === state.uid && !data.answer);
  el("studentBuzz").textContent = buzzText(data);
}

function renderAnswers(container, question, answer, clickable) {
  if (!question) {
    container.innerHTML = "";
    return;
  }
  container.innerHTML = "";
  question.options.forEach((option, index) => {
    const button = document.createElement("button");
    button.className = "answer";
    button.type = "button";
    button.textContent = option;
    button.disabled = !clickable;
    if (answer && index === question.answer) button.classList.add("correct");
    if (answer && answer.choice === index && !answer.correct) button.classList.add("wrong");
    if (clickable) button.addEventListener("click", () => answerQuestion(index));
    container.appendChild(button);
  });
}

function buzzText(data) {
  if (data.status === "ended") return `活動結束。紅隊 ${data.scores?.red || 0} 分，藍隊 ${data.scores?.blue || 0} 分。`;
  if (data.answer) return `${data.answer.name} 已作答：${data.answer.correct ? "答對" : "答錯"}。${data.answer.explain}`;
  if (data.buzz) return `${data.buzz.name}（${data.buzz.team === "red" ? "紅隊" : "藍隊"}）搶到答題權。`;
  if (data.status === "playing") return "開放搶答。";
  return "等待講師開始。";
}

function escapeHtml(value) {
  return String(value).replace(/[&<>"']/g, (char) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#039;" })[char]);
}

function setupEvents() {
  el("hostEntry").addEventListener("click", () => {
    state.role = "host";
    show(loadConfig() ? "hostScreen" : "setupScreen");
  });
  el("studentEntry").addEventListener("click", () => {
    state.role = "student";
    show(loadConfig() ? "studentScreen" : "setupScreen");
  });
  el("saveConfig").addEventListener("click", () => {
    try {
      const config = JSON.parse(el("firebaseConfig").value);
      localStorage.setItem("nutrition_firebase_config", JSON.stringify(config));
      show(state.role === "student" ? "studentScreen" : "hostScreen");
    } catch {
      alert("Firebase 設定不是有效 JSON。");
    }
  });
  el("skipConfig").addEventListener("click", () => show(state.role === "student" ? "studentScreen" : "hostScreen"));
  document.querySelectorAll(".segmented button").forEach((button) => {
    button.addEventListener("click", () => {
      document.querySelectorAll(".segmented button").forEach((item) => item.classList.remove("active"));
      button.classList.add("active");
      state.selectedCount = button.dataset.count === "custom" ? Number(el("customCount").value) : Number(button.dataset.count);
      el("customCount").style.display = button.dataset.count === "custom" ? "block" : "none";
      if (button.dataset.count !== "custom") el("customCount").value = state.selectedCount;
    });
  });
  el("createRoom").addEventListener("click", createRoom);
  el("startRound").addEventListener("click", startRound);
  el("nextQuestion").addEventListener("click", nextQuestion);
  el("endRoom").addEventListener("click", endRoom);
  el("joinRoom").addEventListener("click", joinRoom);
  el("buzzMe").addEventListener("click", buzzMe);
  el("soundToggle").addEventListener("click", () => {
    state.sound = !state.sound;
    el("soundToggle").textContent = state.sound ? "音效" : "靜音";
  });
}

function boot() {
  renderModeOptions();
  document.querySelector("[data-count='10']").classList.add("active");
  el("customCount").style.display = "none";
  setupEvents();
  const config = loadConfig();
  if (params.get("room")) {
    state.role = "student";
    state.room = params.get("room").toUpperCase();
    el("joinCode").value = state.room;
    show(config ? "studentScreen" : "setupScreen");
  }
}

boot();
