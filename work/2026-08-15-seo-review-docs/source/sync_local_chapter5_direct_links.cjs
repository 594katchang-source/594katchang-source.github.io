const fs = require('fs');

const root = process.cwd();
const postsPath = `${root}/blog/posts.json`;
const reviewPath = `${root}/work/2026-08-15-seo-review-docs/source/chapter-05-review.json`;
const reviewHtmlPath = `${root}/work/2026-08-15-seo-review-docs/source/chapter-05-review.html`;
const targetId = '2026-08-20-lipids-fatty-acids-guide';

const replacements = [
  [
    '文章性質：章節整理發文，將原章節概念轉成台灣讀者可使用的脂質判讀方法。',
    '文章性質：章節整理發文，將原章節概念轉成台灣讀者可使用的脂質判讀方法。想先建立食物選擇與健康行為的閱讀框架，可延伸閱讀<a href="https://594katchang-source.github.io/blog/post.html?id=2026-08-14-food-choices-human-health-guide">第一章：Food Choices and Human Health</a>。'
  ],
  [
    '不要把這些名詞混在一起，容易把血液檢驗、食物脂肪與保健品說成同一件事。</p>',
    '不要把這些名詞混在一起，容易把血液檢驗、食物脂肪與保健品說成同一件事。若要先熟悉 DRI、營養標示與營養判讀，可參考<a href="https://594katchang-source.github.io/blog/post.html?id=2026-08-15-nutrition-tools-standards-guidelines">第二章：Nutrition Tools, Standards, and Guidelines</a>。</p>'
  ],
  [
    '此外，脂肪品質要連同整份食物與飲食型態一起看。</p>',
    '此外，脂肪品質要連同整份食物與飲食型態一起看。醣類來源、膳食纖維與脂質替代也可搭配閱讀<a href="https://594katchang-source.github.io/blog/post.html?id=2026-08-17-carbohydrates-food-guide">第四章：碳水化合物怎麼吃才穩？</a>。</p>'
  ]
];

function patchBody(body) {
  if ((body.match(/<a\s+href=/gi) || []).length === 6) return body;
  let next = body;
  for (const [from, to] of replacements) {
    const count = next.split(from).length - 1;
    if (count !== 1) throw new Error(`Expected one replacement match, got ${count}`);
    next = next.replace(from, to);
  }
  const anchors = (next.match(/<a\s+href=/gi) || []).length;
  if (anchors !== 6) throw new Error(`Expected 6 body links, got ${anchors}`);
  return next;
}

function unpatchBody(body) {
  let old = body;
  for (const [from, to] of [...replacements].reverse()) {
    const count = old.split(to).length - 1;
    if (count !== 1) throw new Error(`Expected one reverse replacement match, got ${count}`);
    old = old.replace(to, from);
  }
  return old;
}

const posts = JSON.parse(fs.readFileSync(postsPath, 'utf8'));
const post = posts.posts.find(item => item.id === targetId);
if (!post) throw new Error('Local target post missing');
const oldPostBody = post.body;
post.body = patchBody(post.body);
fs.writeFileSync(postsPath, JSON.stringify(posts, null, 2) + '\n', 'utf8');

const review = JSON.parse(fs.readFileSync(reviewPath, 'utf8'));
review.bodyHtml = patchBody(review.bodyHtml);
const reviewHtml = fs.readFileSync(reviewHtmlPath, 'utf8');
let updatedReviewHtml = reviewHtml;
for (const [from, to] of replacements) {
  const count = updatedReviewHtml.split(from).length - 1;
  if (count !== 1) throw new Error(`Review HTML replacement match not unique: ${count}`);
  updatedReviewHtml = updatedReviewHtml.replace(from, to);
}
fs.writeFileSync(reviewPath, JSON.stringify(review, null, 2) + '\n', 'utf8');
fs.writeFileSync(reviewHtmlPath, updatedReviewHtml, 'utf8');

console.log(JSON.stringify({
  targetId,
  oldPostLength: oldPostBody.length,
  newPostLength: post.body.length,
  reviewBodyLength: review.bodyHtml.length,
  newReviewLength: review.bodyHtml.length,
  bodyLinks: 6,
  docxUnchanged: true
}));
