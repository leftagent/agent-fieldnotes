const fs=require('node:fs'),vm=require('node:vm'),assert=require('node:assert/strict'),path=require('node:path');
const read=n=>fs.readFileSync(path.join(__dirname,n),'utf8'),xml=read('sitemap.xml'),urls=[...xml.matchAll(/<loc>(.*?)<\/loc>/g)].map(m=>m[1]);
assert.equal(urls.length,16);assert.equal(new Set(urls).size,16);
const decode=s=>s.replace(/&quot;/g,'"').replace(/&#39;/g,"'").replace(/&lt;/g,'<').replace(/&gt;/g,'>').replace(/&amp;/g,'&');
for(const url of urls){const name=url.split('/').pop(),html=read(name);assert(!/[?#]/.test(url));assert.equal([...html.matchAll(/rel="canonical"/g)].length,1);assert(html.includes(`rel="canonical" href="${url}"`));assert(!/noindex/i.test(html));for(const lang of ['zh-CN','en','x-default'])assert(html.includes(`hreflang="${lang}"`));for(const m of html.matchAll(/(?:href|src)="\.\/([^"?#]+)(?:[?#][^"]*)?"/g))assert(fs.existsSync(path.join(__dirname,m[1])),name+' broken '+m[1]);
 for(const m of html.matchAll(/<script([^>]*)>([\s\S]*?)<\/script>/g)){if(m[1].includes('ld+json'))assert.equal(JSON.parse(m[2])['@type'],'TechArticle');else new vm.Script(m[2]);}
}
for(const lang of ['zh','en']){const suffix=lang==='en'?'-en':'',h=read('index'+suffix+'.html'),c={window:{}};vm.createContext(c);vm.runInContext([...h.matchAll(/<script>([\s\S]*?)<\/script>/g)].map(m=>m[1]).find(s=>s.includes('window.HANDBOOK =')),c);
 for(const [slug,ids] of Object.entries({'agent-loop':['loop'],'mcp-tutorial':['mcp'],'hitl-checkpoint':['checkpoint','interrupt'],'langgraph-tutorial':['state','routing','parallel']})){const page=read(slug+suffix+'.html'),visible=decode(page.replace(/<script[\s\S]*?<\/script>/g,'').replace(/<[^>]+>/g,''));assert(h.includes('./'+slug+suffix+'.html'));assert.equal((page.match(/<h1>/g)||[]).length,1);for(const id of ids){const ch=c.window.HANDBOOK.chapters.find(c=>c.id===id);for(const text of [ch.why,ch.example,ch.code,ch.pitfall,...ch.steps,...ch.notes,...ch.tests])assert(visible.includes(text),slug+' missing static text '+id);}}
}
console.log('PASS: 16 unique sitemap URLs, canonical/hreflang, local links, script/schema syntax, 8 full-text tutorials containing all 7 source chapters in both languages.');
