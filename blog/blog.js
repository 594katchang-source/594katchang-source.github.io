const STOPWORDS=new Set('的 了 與 和 或 是 在 有 我 你 他 她 它 們 一個 以及 這個 那個 如何 可以 透過 關於 來源 年的 皮膚 多少 知多少 問題 症狀 常見 使用 文章 內文'.split(' '));
const DOMAIN_TERMS=['食物過敏','過敏原','免疫系統','IgE','非IgE','過敏性休克','蕁麻疹','血管性水腫','呼吸困難','營養','蛋白質','膳食纖維','全穀雜糧','蔬果','血糖','早餐','中高齡','高齡健康','肌少症','骨質疏鬆','糖尿病','高血壓','腸胃道','健康管理','臨床營養'];
const SAFE_TAGS=new Set(['P','H2','H3','STRONG','EM','UL','OL','LI','BLOCKQUOTE','A','IMG','BR','SPAN','CODE','PRE','TABLE','THEAD','TBODY','TR','TH','TD']);
const SAFE_ATTRS={A:new Set(['href','title','target','rel']),IMG:new Set(['src','alt','title']),SPAN:new Set(['class']),TH:new Set(['colspan','rowspan']),TD:new Set(['colspan','rowspan'])};
function escapeHtml(value=''){return String(value).replace(/[&<>"']/g,char=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#039;'}[char]))}
function safeUrl(value,kind='href'){const raw=String(value||'').trim();if(!raw)return'';if(/^https?:\/\//i.test(raw)||raw.startsWith('/')||raw.startsWith('./')||raw.startsWith('../')||raw.startsWith('#')||kind==='src'&&raw.startsWith('data:image/'))return raw;return''}
function normalizeTextBreaks(root){const walker=document.createTreeWalker(root,NodeFilter.SHOW_TEXT);const nodes=[];while(walker.nextNode())nodes.push(walker.currentNode);const blockTags=new Set(['P','H2','H3','UL','OL','LI','BLOCKQUOTE','TABLE','THEAD','TBODY','TR','TH','TD','PRE']);nodes.forEach(node=>{const raw=node.nodeValue||'';const text=raw.replace(/\\n/g,'\n');if(text===raw&&!text.includes('\n'))return;const parent=node.parentElement;const prev=node.previousSibling?.nodeType===1?node.previousSibling.tagName:'';const next=node.nextSibling?.nodeType===1?node.nextSibling.tagName:'';if(!text.replace(/\s/g,'').length){if(blockTags.has(parent?.tagName)||(blockTags.has(prev)&&blockTags.has(next))){node.remove();return}}if(!text.includes('\n')){node.nodeValue=text;return}const fragment=document.createDocumentFragment();text.split('\n').forEach((part,index)=>{if(index)fragment.appendChild(document.createElement('br'));if(part)fragment.appendChild(document.createTextNode(part))});node.replaceWith(fragment)})}
function sanitizeHtml(value=''){const template=document.createElement('template');template.innerHTML=String(value).replace(/\\n/g,'\n');const clean=(node)=>{[...node.children].forEach(child=>{if(!SAFE_TAGS.has(child.tagName)){child.replaceWith(document.createTextNode(child.textContent||''));return} [...child.attributes].forEach(attr=>{const allowed=SAFE_ATTRS[child.tagName]?.has(attr.name);if(!allowed){child.removeAttribute(attr.name);return}if(attr.name==='href'||attr.name==='src'){const url=safeUrl(attr.value,attr.name);if(url)child.setAttribute(attr.name,url);else child.removeAttribute(attr.name)}});if(child.tagName==='A'&&child.getAttribute('target')==='_blank')child.setAttribute('rel','noopener');if(child.tagName==='SPAN'&&child.classList.contains('source-ref'))child.setAttribute('class','source-ref');else if(child.tagName==='SPAN')child.removeAttribute('class');clean(child)})};clean(template.content);normalizeTextBreaks(template.content);return template.innerHTML}
function stripHtml(s=''){return String(s).replace(/<script[\s\S]*?<\/script>/gi,' ').replace(/<style[\s\S]*?<\/style>/gi,' ').replace(/<[^>]*>/g,' ').replace(/&[^;]+;/g,' ').replace(/\[來源\d+(?:,\s*\d+)*\]/g,' ').replace(/\s+/g,' ').trim()}
function summary(post){const given=stripHtml(post.excerpt||'');if(given.length>=24)return truncate(given,96);const text=stripHtml(post.body||'');const sentence=(text.match(/[^。！？!?]{24,130}[。！？!?]/)||[text.slice(0,118)])[0];return truncate(sentence,96)}
function keywords(post){if(Array.isArray(post.keywords)&&post.keywords.length)return post.keywords.slice(0,5);const text=[post.title,post.excerpt,stripHtml(post.body)].join(' ');const found=[];for(const term of DOMAIN_TERMS){if(text.toLowerCase().includes(term.toLowerCase()))found.push(term)}const headings=[...(post.body||'').matchAll(/<h[2-3][^>]*>(.*?)<\/h[2-3]>/gi)].map(m=>stripHtml(m[1])).filter(Boolean);const titleParts=String(post.title||'').replace(/[？?！!]/g,'').split(/[：:、，,\s-]+/).filter(w=>w.length>=2&&w.length<=8);const words=(stripHtml(text).match(/[\u4e00-\u9fa5]{2,6}|[A-Za-z][A-Za-z-]{2,}/g)||[]).filter(w=>!STOPWORDS.has(w)&&!/來源|\d/.test(w));const score=new Map();[...found,...headings,...titleParts,...words].forEach((w,i)=>{const key=w.trim();if(!key||STOPWORDS.has(key))return;score.set(key,(score.get(key)||0)+(i<found.length?6:1))});return [...score.entries()].sort((a,b)=>b[1]-a[1]||a[0].length-b[0].length).slice(0,5).map(([w])=>w)}
function truncate(text,max){return text.length>max?`${text.slice(0,max-1)}…`:text}
function postDate(post){const value=Date.parse(`${String(post.date||'').slice(0,10)}T00:00:00`);return Number.isNaN(value)?0:value}
function sortPosts(posts){return posts.map((post,index)=>({post,index})).sort((a,b)=>postDate(b.post)-postDate(a.post)||a.index-b.index).map(item=>item.post)}
function categoryName(post){const value=String(post.category||'').trim();return value||'未分類'}
function postMeta(post){return [post.date,post.category?categoryName(post):''].filter(Boolean).join('｜')}
function searchValue(post){return [post.title,post.excerpt,post.body,post.category,...(Array.isArray(post.keywords)?post.keywords:[])].map(value=>stripHtml(value||'')).join(' ').toLocaleLowerCase()}
function imageSrc(post){const raw=String(post.image||'').trim();if(!raw)return'images/default.svg';if(/^https?:\/\//i.test(raw)||raw.startsWith('/'))return safeUrl(raw,'src')||'images/default.svg';if(raw.startsWith('blog/images/'))return raw.replace(/^blog\//,'');if(raw.startsWith('images/'))return raw;return `images/${encodeURIComponent(raw).replace(/%2F/g,'/')}`}
function card(post){return `<a class="post-card" href="post.html?id=${encodeURIComponent(post.id)}"><img class="post-thumb" src="${escapeHtml(imageSrc(post))}" alt=""><div><div class="post-meta">${escapeHtml(postMeta(post))}</div><h3>${escapeHtml(post.title||'')}</h3><p>${escapeHtml(summary(post))}</p><div class="keywords">${keywords(post).map(k=>`<span>${escapeHtml(k)}</span>`).join('')}</div></div></a>`}
function renderDirectory(posts){
  const list=document.querySelector('#posts');
  const search=document.querySelector('#post-search');
  const category=document.querySelector('#post-category');
  const result=document.querySelector('#post-results');
  const clear=document.querySelector('#clear-post-filters');
  if(!list||!search||!category||!result||!clear)return;
  const ordered=sortPosts(posts);
  [...new Set(ordered.map(categoryName))].sort((a,b)=>a.localeCompare(b,'zh-Hant')).forEach(name=>{const option=document.createElement('option');option.value=name;option.textContent=name;category.append(option)});
  const update=()=>{
    const query=search.value.trim().toLocaleLowerCase();
    const selectedCategory=category.value;
    const filtered=ordered.filter(post=>(!selectedCategory||categoryName(post)===selectedCategory)&&(!query||searchValue(post).includes(query)));
    list.innerHTML=filtered.map(card).join('')||'<p class="post-empty">找不到符合條件的文章，請換一個關鍵字或清除篩選。</p>';
    result.textContent=query||selectedCategory?`符合條件的文章：${filtered.length} 篇，共 ${posts.length} 篇`:`共 ${posts.length} 篇文章，依日期由新到舊排列`;
    clear.hidden=!query&&!selectedCategory;
  };
  search.addEventListener('input',update);
  search.addEventListener('keydown',event=>{if(event.key==='Escape'){search.value='';category.value='';update();search.focus()}});
  category.addEventListener('change',update);
  clear.addEventListener('click',()=>{search.value='';category.value='';update();search.focus()});
  update();
}
function setMeta(selector,attrs){let el=document.head.querySelector(selector);if(!el){el=document.createElement('meta');document.head.appendChild(el)}Object.entries(attrs).forEach(([key,value])=>el.setAttribute(key,value))}
function setArticleSeo(post){
  const url=`${location.origin}${location.pathname}?id=${encodeURIComponent(post.id)}`;
  const description=summary(post);
  const image=new URL(imageSrc(post),location.href).href;
  document.title=`${post.title} | Kat Chang 凱特營養師`;
  let canonical=document.head.querySelector('link[rel="canonical"]');
  if(!canonical){canonical=document.createElement('link');canonical.rel='canonical';document.head.appendChild(canonical)}
  canonical.href=url;
  setMeta('meta[name="description"]',{name:'description',content:description});
  setMeta('meta[name="robots"]',{name:'robots',content:'index, follow, max-image-preview:large, max-snippet:-1'});
  setMeta('meta[property="og:type"]',{property:'og:type',content:'article'});
  setMeta('meta[property="og:title"]',{property:'og:title',content:post.title});
  setMeta('meta[property="og:description"]',{property:'og:description',content:description});
  setMeta('meta[property="og:url"]',{property:'og:url',content:url});
  setMeta('meta[property="og:image"]',{property:'og:image',content:image});
  setMeta('meta[property="article:published_time"]',{property:'article:published_time',content:post.date});
  let jsonLd=document.querySelector('#article-jsonld');
  if(!jsonLd){jsonLd=document.createElement('script');jsonLd.type='application/ld+json';jsonLd.id='article-jsonld';document.head.appendChild(jsonLd)}
  jsonLd.textContent=JSON.stringify({'@context':'https://schema.org','@type':'BlogPosting',headline:post.title,description,image:[image],datePublished:post.date,dateModified:post.date,articleSection:post.category||undefined,keywords:(post.keywords||[]).join(', '),mainEntityOfPage:url,author:{'@type':'Person',name:'張雁雲營養師',alternateName:'Kat Chang 凱特營養師',url:'https://594katchang-source.github.io/about.html'},publisher:{'@type':'Person',name:'張雁雲營養師',url:'https://594katchang-source.github.io/'}});
  let faqLd=document.querySelector('#faq-jsonld');
  if(post.faq&&Array.isArray(post.faq)&&post.faq.length){
    if(!faqLd){faqLd=document.createElement('script');faqLd.type='application/ld+json';faqLd.id='faq-jsonld';document.head.appendChild(faqLd)}
    faqLd.textContent=JSON.stringify({'@context':'https://schema.org','@type':'FAQPage',mainEntity:post.faq.map(item=>({'@type':'Question',name:item.question,acceptedAnswer:{'@type':'Answer',text:item.answer}}))});
  }else if(faqLd)faqLd.remove();
}

function renderRelatedPosts(currentPost, allPosts) {
  const otherPosts = allPosts.filter(p => p.id !== currentPost.id);
  if (!otherPosts.length) return '';
  const matched = otherPosts.filter(p => p.category === currentPost.category);
  const candidates = (matched.length >= 2 ? matched : otherPosts).slice(0, 3);
  return `
    <section class="related-posts-section" style="margin-top:48px;padding-top:32px;border-top:1px solid var(--line);">
      <h2 style="font-size:1.4rem;color:var(--green-dark);margin-bottom:20px;">💡 延伸閱讀・精選衛教文章</h2>
      <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:16px;">
        ${candidates.map(p => `
          <a class="service-card" href="post.html?id=${encodeURIComponent(p.id)}" style="display:block;text-decoration:none;padding:18px;border-radius:18px;">
            <div style="font-size:0.85rem;color:var(--muted);margin-bottom:6px;">${escapeHtml(p.date || '')}</div>
            <h3 style="font-size:1.05rem;line-height:1.4;margin-bottom:8px;color:var(--ink);">${escapeHtml(p.title || '')}</h3>
            <p style="font-size:0.9rem;color:var(--muted);margin:0;">${escapeHtml(summary(p))}</p>
          </a>
        `).join('')}
      </div>
    </section>
  `;
}

async function main(){const res=await fetch('posts.json?v=20260815-blog-directory',{cache:'no-store'});const posts=(await res.json()).posts||[];const list=document.querySelector('#posts');if(list){renderDirectory(posts);return}const article=document.querySelector('#article');if(article){const id=new URLSearchParams(location.search).get('id');const post=posts.find(p=>p.id===id)||posts[0];if(!post){article.innerHTML='<p>找不到文章。</p>';return}setArticleSeo(post);article.innerHTML=`<a class="back-link" href="./">← 返回文章列表</a><div class="post-meta">${escapeHtml(post.date||'')}｜作者：<a href="../about.html">張雁雲營養師</a></div><h1>${escapeHtml(post.title||'')}</h1><div class="keywords">${keywords(post).map(k=>`<span>${escapeHtml(k)}</span>`).join('')}</div>${post.image?`<img class="article-cover" src="${escapeHtml(imageSrc(post))}" alt="${escapeHtml(post.title||'')}">`:''}<div class="article-body">${sanitizeHtml(post.body||'')}</div>${renderRelatedPosts(post, posts)}`}}main().catch(()=>{const el=document.querySelector('#posts,#article');if(el)el.innerHTML='<p>內容載入失敗。</p>'});

