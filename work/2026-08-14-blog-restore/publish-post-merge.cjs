const fs = require('node:fs');
const path = require('node:path');
const { execFileSync } = require('node:child_process');

const root = path.resolve(__dirname, '..', '..');
const outputDir = path.join(__dirname, 'output');
const endpoint = 'repos/594katchang-source/594katchang-source.github.io/contents/blog/posts.json';
const postsPath = path.join(root, 'blog', 'posts.json');
const articleId = '2026-08-13-nutrition-concepts-controversies-17e-guide';

function gh(args, input) {
  return execFileSync('gh', ['api', ...args], {
    cwd: root,
    encoding: 'utf8',
    input,
    maxBuffer: 8 * 1024 * 1024
  });
}

function readRemote() {
  const result = JSON.parse(gh([endpoint, '-f', 'ref=main']));
  const content = Buffer.from(result.content.replace(/\s/g, ''), 'base64').toString('utf8');
  return { result, content, data: JSON.parse(content) };
}

const local = JSON.parse(fs.readFileSync(postsPath, 'utf8'));
const desired = local.posts.find((post) => post.id === articleId);
if (!desired || desired.showOnHome !== false || desired.image !== 'images/2026-08-13-nutrition-concepts-controversies-17e-guide.png') {
  throw new Error('Local restore source does not contain the expected target article state.');
}

const before = readRemote();
const remoteIndex = before.data.posts.findIndex((post) => post.id === articleId);
if (remoteIndex < 0) throw new Error('Remote target article was not found.');
before.data.posts[remoteIndex] = desired;
const mergedContent = `${JSON.stringify(before.data, null, 2)}\n`;
fs.mkdirSync(outputDir, { recursive: true });
fs.writeFileSync(path.join(outputDir, 'posts-remote-before-put.json'), before.content, 'utf8');

const payload = JSON.stringify({
  message: 'Restore reviewed blog post and preserve homepage selection',
  content: Buffer.from(mergedContent, 'utf8').toString('base64'),
  sha: before.result.sha,
  branch: 'main'
});
const putResult = JSON.parse(gh([endpoint, '--method', 'PUT', '--input', '-'], payload));

const after = readRemote();
const restored = after.data.posts.find((post) => post.id === articleId);
if (restored.title !== desired.title || restored.body !== desired.body || restored.image !== desired.image || restored.showOnHome !== false) {
  throw new Error('Remote verification failed after PUT.');
}
fs.writeFileSync(path.join(outputDir, 'posts-remote-after-put.json'), after.content, 'utf8');

console.log(JSON.stringify({
  commit: putResult.commit?.sha || null,
  remoteFileSha: after.result.sha,
  postCount: after.data.posts.length,
  homeCount: after.data.posts.filter((post) => post.showOnHome === true).length,
  restored: {
    id: restored.id,
    title: restored.title,
    image: restored.image,
    showOnHome: restored.showOnHome,
    bodyLength: restored.body.length
  }
}, null, 2));
