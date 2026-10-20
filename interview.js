(() => {
  'use strict';
  const zh = document.documentElement.lang.startsWith('zh');
  const t = (a,b) => zh ? a : b;
  const articles = [...document.querySelectorAll('.answer')];
  const links = [...document.querySelectorAll('.question-link')];
  const byId = new Map(articles.map(a => [a.id,a]));
  const search = document.querySelector('#search');
  const category = document.querySelector('#category');
  const unread = document.querySelector('#unread-only');
  const key = 'agent-fieldnotes-interview-learned-v1';
  let learned = new Set();
  try { const saved=JSON.parse(localStorage.getItem(key)||'[]'); if(Array.isArray(saved)) learned = new Set(saved.filter(id=>byId.has(id))); } catch (_) {}
  const searchable = new Map(articles.map(a=>[a.id,a.textContent.toLocaleLowerCase()]));
  let toastTimer;
  function toast(text) { const el=document.querySelector('#toast'); el.textContent=text; clearTimeout(toastTimer); toastTimer=setTimeout(()=>el.textContent='',2800); }
  function languageLinks() { document.querySelectorAll('[data-language]').forEach(a=>{const u=new URL(a.href);u.hash=location.hash;a.href=u.href;}); }
  function currentId() { try { return decodeURIComponent(location.hash.slice(1)); } catch (_) { return ''; } }
  function select(id,scroll=false) {
    if (!byId.has(id)) id=articles[0].id;
    articles.forEach(a=>a.hidden=a.id!==id);
    links.forEach(a=>a.setAttribute('aria-current',String(a.hash==='#'+id)));
    languageLinks();
    if(scroll) { byId.get(id).scrollIntoView({block:'start'}); byId.get(id).querySelector('h2').focus({preventScroll:true}); }
  }
  function filter() {
    const terms=search.value.trim().toLocaleLowerCase().split(/\s+/).filter(Boolean);
    let count=0;
    links.forEach(a=>{
      const id=a.hash.slice(1);
      a.hidden=!( (category.value==='all'||a.dataset.category===category.value) && (!unread.checked||!learned.has(id)) && terms.every(s=>searchable.get(id).includes(s)) );
      if(!a.hidden)count++;
    });
    document.querySelector('#result-count').textContent=String(count);
    document.querySelector('#result-count').setAttribute('aria-label',t(`${count} 道匹配题目`,`${count} matching questions`));
    document.querySelector('#no-results').hidden=count>0;
    document.querySelectorAll('.category-chip').forEach(b=>b.setAttribute('aria-pressed',String(category.value===b.dataset.category)));
  }
  function updateProgress() {
    document.querySelector('#study-progress').value=learned.size;
    document.querySelector('#progress-label').textContent=`${learned.size} / 96`;
    articles.forEach(a=>{const yes=learned.has(a.id),b=a.querySelector('.mark-read');b.setAttribute('aria-pressed',String(yes));b.textContent=yes?t('✓ 已掌握','✓ Learned'):t('标记掌握','Mark learned');});
    links.forEach(a=>a.classList.toggle('learned',learned.has(a.hash.slice(1))));
    filter();
  }
  async function copy(text) { try { await navigator.clipboard.writeText(text); toast(t('已复制','Copied')); } catch (_) { toast(t('复制不可用，请手动复制','Copy unavailable; please copy manually')); } }
  document.documentElement.classList.add('js');
  select(currentId()); updateProgress();
  window.addEventListener('hashchange',()=>select(currentId(),byId.has(currentId())));
  search.addEventListener('input',filter); category.addEventListener('change',filter); unread.addEventListener('change',filter);
  document.querySelector('#clear-search').addEventListener('click',()=>{search.value='';filter();search.focus();});
  document.querySelectorAll('.category-chip').forEach(b=>b.addEventListener('click',()=>{category.value=b.dataset.category;search.value='';filter();document.querySelector('#questions').scrollIntoView({block:'start'});}));
  document.querySelector('#show-all').addEventListener('click',()=>{category.value='all';search.value='';unread.checked=false;filter();document.querySelector('#questions').scrollIntoView({block:'start'});});
  document.querySelectorAll('.question-link,.question-pager a').forEach(a=>a.addEventListener('click',()=>{if(a.hash===location.hash)select(a.hash.slice(1),true);}));
  articles.forEach(a=>{
    a.querySelector('.mark-read').addEventListener('click',()=>{learned.has(a.id)?learned.delete(a.id):learned.add(a.id);try{localStorage.setItem(key,JSON.stringify([...learned]));}catch(_){toast(t('浏览器无法保存，进度仅在本次打开有效','Storage unavailable; progress lasts for this visit'));}updateProgress();});
    a.querySelector('.copy-link').addEventListener('click',()=>{const u=new URL(location.href);u.hash=a.id;copy(u.href);});
    const b=a.querySelector('.copy-code');if(b)b.addEventListener('click',()=>copy(a.querySelector('code').textContent));
  });
  document.querySelectorAll('[data-language]').forEach(a=>a.addEventListener('click',()=>{languageLinks();try{localStorage.setItem('agent-fieldnotes-language',a.dataset.language);}catch(_){}}));
  window.addEventListener('storage',e=>{if(e.key===key){try{const saved=JSON.parse(e.newValue||'[]');learned=new Set(Array.isArray(saved)?saved.filter(id=>byId.has(id)):[]);updateProgress();}catch(_){}}});
})();
