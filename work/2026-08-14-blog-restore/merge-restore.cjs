const fs = require('node:fs');
const path = require('node:path');
const { execFileSync } = require('node:child_process');

const root = path.resolve(__dirname, '..', '..');
const postsPath = path.join(root, 'blog', 'posts.json');
const outputDir = path.join(__dirname, 'output');
const articleId = '2026-08-13-nutrition-concepts-controversies-17e-guide';

const currentRaw = fs.readFileSync(postsPath, 'utf8');
const current = JSON.parse(currentRaw);
const headRaw = execFileSync('git', ['show', 'HEAD:blog/posts.json'], { cwd: root, encoding: 'utf8' });
const head = JSON.parse(headRaw);
const desired = head.posts.find((post) => post.id === articleId);
const currentIndex = current.posts.findIndex((post) => post.id === articleId);

if (!desired || currentIndex < 0) throw new Error('Target article was not found in HEAD and current posts.json.');
if (desired.showOnHome !== false || desired.image !== 'images/2026-08-13-nutrition-concepts-controversies-17e-guide.png') {
  throw new Error('HEAD does not contain the expected reviewed article state.');
}

fs.mkdirSync(outputDir, { recursive: true });
fs.writeFileSync(path.join(outputDir, 'posts-before-restore.json'), currentRaw, 'utf8');
current.posts[currentIndex] = desired;
fs.writeFileSync(postsPath, `${JSON.stringify(current, null, 2)}\n`, 'utf8');

console.log(JSON.stringify({
  articleId,
  postCount: current.posts.length,
  restoredTitle: desired.title,
  restoredImage: desired.image,
  restoredShowOnHome: desired.showOnHome,
  preservedOtherPostIds: current.posts.filter((post) => post.id !== articleId).map((post) => post.id)
}, null, 2));
