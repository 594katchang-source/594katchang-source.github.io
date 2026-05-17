const OWNER = '594katchang-source';
const REPO = '594katchang-source.github.io';
const BRANCH = 'main';
const POSTS_PATH = 'blog/posts.json';
const API = `https://api.github.com/repos/${OWNER}/${REPO}/contents/`;

const form = document.querySelector('#editor');
const statusBox = document.querySelector('#status');
const previewBox = document.querySelector('#preview');
const dateInput = document.querySelector('#date');
const titleInput = document.querySelector('#title');
const slugInput = document.querySelector('#slug');

dateInput.valueAsDate = new Date();

titleInput.addEventListener('input', () => {
  if (slugInput.dataset.touched) return;
  slugInput.value = slugify(titleInput.value);
});
slugInput.addEventListener('input', () => { slugInput.dataset.touched = '1'; });
document.querySelector('#previewBtn').addEventListener('click', renderPreview);

form.addEventListener('submit', async (event) => {
  event.preventDefault();
  setStatus('準備發布...');
  const data = readForm();
  try {
    if (!data.token.startsWith('github_') && !data.token.startsWith('ghp_')) throw new Error('GitHub token 格式看起來不正確。');
    setStatus('讀取現有文章資料...');
    const postsFile = await githubGet(POSTS_PATH, data.token);
    const postsData = JSON.parse(decodeBase64Utf8(postsFile.content));
    const posts = Array.isArray(postsData.posts) ? postsData.posts : [];
    if (posts.some(post => post.id === data.slug)) throw new Error(`文章 ID 已存在：${data.slug}`);

    let imagePath = '';
    if (data.imageFile) {
      setStatus('上傳圖片...');
      const ext = extensionFromFile(data.imageFile);
      imagePath = `blog/images/${data.slug}.${ext}`;
      const imageBase64 = await fileToBase64(data.imageFile);
      await githubPut(imagePath, data.token, {
        message: `Add blog image ${data.slug}`,
        content: imageBase64,
        branch: BRANCH
      });
    }

    const newPost = {
      id: data.slug,
      title: data.title,
      date: data.date,
      image: imagePath ? imagePath.replace(/^blog\//, '') : '',
      excerpt: data.excerpt,
      body: normalizeBody(data.body)
    };
    posts.unshift(newPost);

    setStatus('更新文章列表...');
    await githubPut(POSTS_PATH, data.token, {
      message: `Add blog post ${data.slug}`,
      content: encodeBase64Utf8(JSON.stringify({ posts }, null, 2) + '\n'),
      sha: postsFile.sha,
      branch: BRANCH
    });

    setStatus(`發布完成。\n文章網址：../blog/post.html?id=${encodeURIComponent(data.slug)}`);
    form.reset();
    dateInput.valueAsDate = new Date();
    previewBox.innerHTML = '';
  } catch (error) {
    setStatus(`發布失敗：${error.message}`);
  }
});

function readForm() {
  return {
    token: document.querySelector('#token').value.trim(),
    title: titleInput.value.trim(),
    date: dateInput.value,
    slug: slugify(slugInput.value),
    excerpt: document.querySelector('#excerpt').value.trim(),
    body: document.querySelector('#body').value.trim(),
    imageFile: document.querySelector('#image').files[0]
  };
}

function renderPreview() {
  const data = readForm();
  const html = normalizeBody(data.body);
  previewBox.innerHTML = `<article class="post-card"><div><div class="post-meta">${escapeHtml(data.date)}</div><h3>${escapeHtml(data.title || '未命名文章')}</h3><p>${escapeHtml(data.excerpt)}</p><div class="article-body">${html}</div></div></article>`;
}

function normalizeBody(body) {
  if (/<[a-z][\s\S]*>/i.test(body)) return body;
  return body.split(/\n\s*\n/).map(p => `<p>${escapeHtml(p).replace(/\n/g, '<br>')}</p>`).join('');
}

async function githubGet(path, token) {
  const res = await fetch(`${API}${path}?ref=${BRANCH}`, { headers: authHeaders(token) });
  if (!res.ok) throw new Error(`GitHub 讀取失敗 ${res.status}: ${await res.text()}`);
  return res.json();
}

async function githubPut(path, token, payload) {
  const res = await fetch(`${API}${path}`, {
    method: 'PUT',
    headers: { ...authHeaders(token), 'Content-Type': 'application/json' },
    body: JSON.stringify(payload)
  });
  if (!res.ok) throw new Error(`GitHub 寫入失敗 ${res.status}: ${await res.text()}`);
  return res.json();
}

function authHeaders(token) {
  return {
    Authorization: `Bearer ${token}`,
    Accept: 'application/vnd.github+json',
    'X-GitHub-Api-Version': '2022-11-28'
  };
}

function slugify(value) {
  return value.trim().toLowerCase().replace(/[^a-z0-9\u4e00-\u9fa5]+/g, '-').replace(/^-+|-+$/g, '').slice(0, 80);
}

function extensionFromFile(file) {
  const byName = file.name.split('.').pop()?.toLowerCase();
  if (byName && /^[a-z0-9]+$/.test(byName)) return byName === 'jpeg' ? 'jpg' : byName;
  const byType = file.type.split('/').pop();
  return byType || 'png';
}

function fileToBase64(file) {
  return new Promise((resolve, reject) => {
    const reader = new FileReader();
    reader.onload = () => resolve(String(reader.result).split(',')[1]);
    reader.onerror = () => reject(reader.error);
    reader.readAsDataURL(file);
  });
}

function encodeBase64Utf8(value) {
  return btoa(unescape(encodeURIComponent(value)));
}

function decodeBase64Utf8(value) {
  return decodeURIComponent(escape(atob(value.replace(/\n/g, ''))));
}

function escapeHtml(value) {
  return String(value).replace(/[&<>"']/g, char => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#039;' }[char]));
}

function setStatus(message) {
  statusBox.textContent = message;
  statusBox.classList.add('show');
}
