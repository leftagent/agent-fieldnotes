"""Build the two static interview pages. Run: python build-interview.py."""
import json
from pathlib import Path
from html import escape as esc
ROOT = Path(__file__).resolve().parent
DATA = json.loads((ROOT / 'interview-data.json').read_text())
CATEGORIES = [
 ('foundations','模型与基础','Models & foundations'),('architecture','Agent 架构','Agent architecture'),
 ('prompt','提示与上下文','Prompts & context'),('rag','RAG 与检索','RAG & retrieval'),
 ('tools','工具与 MCP','Tools & MCP'),('memory','状态与记忆','State & memory'),
 ('planning','规划与推理','Planning & reasoning'),('multi','多 Agent 协作','Multi-agent systems'),
 ('evaluation','评测与可观测性','Evaluation & observability'),('safety','安全与权限','Security & permissions'),
 ('production','生产部署','Production engineering'),('projects','项目与手写题','Projects & coding')]
BASE='https://leftagent.github.io/agent-fieldnotes/'
for lang in ['zh','en']:
 zh=lang=='zh'; suffix='' if zh else '-en'; filename='interview'+suffix+'.html'
 def t(a,b): return a if zh else b
 def h(s): return esc(str(s),quote=True)
 names={c: a if zh else b for c,a,b in CATEGORIES}
 ordered=[q for c,_,_ in CATEGORIES for q in DATA if q['category']==c]
 links=[]; articles=[]
 for i,q in enumerate(ordered,1):
  qid=q['id']; title=q['title'][lang]
  links.append(f'<a class="question-link" data-category="{q["category"]}" href="#{qid}"><span>{i:02}</span><span>{h(title)}</span><span class="read-dot" aria-hidden="true"></span></a>')
  reasoning=''.join(f'<li><p>{h(p)}</p></li>' for p in q['reasoning'][lang])
  sources=''.join(f'<a href="{h(url)}" target="_blank" rel="noopener noreferrer">{h(url.split("/")[3]+" / "+url.split("/")[-1].removesuffix(".md"))} ↗</a>' for url in q['sources'])
  code=''
  if q.get('code'):
   code=f'<section><h3>{t("代码示例","Code example")}</h3><div class="code-head"><span>{h(q["code"]["language"])}</span><button class="copy-code" type="button">{t("复制代码","Copy code")}</button></div><pre><code>{h(q["code"]["text"])}</code></pre></section>'
  sections=''.join(f'<section class="{key}"><h3>{label}</h3><p>{h(q[key][lang])}</p></section>' for key,label in [('example',t('工程例子','Engineering example')),('followup',t('面试追问','Follow-up')),('pitfall',t('易错点','Common pitfall'))])
  articles.append(f'''<article class="answer" id="{qid}" data-category="{q['category']}" aria-labelledby="title-{qid}">
 <div class="answer-meta"><span>{i:02} / 96 · {h(names[q['category']])}</span><div class="answer-actions"><button class="copy-link" type="button">{t('复制链接','Copy link')}</button><button class="mark-read" type="button" aria-pressed="false">{t('标记掌握','Mark learned')}</button></div></div>
 <h2 id="title-{qid}" tabindex="-1">{h(title)}</h2>
 <section class="core"><h3>{t('核心回答','Core answer')}</h3><p>{h(q['summary'][lang])}</p></section>
 <section><h3>{t('原理与实现','Reasoning & implementation')}</h3><ol class="reasoning">{reasoning}</ol></section>{sections}{code}
 <section class="references"><h3>{t('延伸阅读','Further reading')}</h3>{sources}</section>
 <div class="question-pager"><a href="#{ordered[max(0,i-2)]['id']}" {'hidden' if i==1 else ''}>← {t('上一题','Previous')}</a><a href="#{ordered[min(95,i)]['id']}" {'hidden' if i==96 else ''}>{t('下一题','Next')} →</a></div></article>''')
 options=''.join(f'<option value="{c}">{h(names[c])} · 8</option>' for c,_,_ in CATEGORIES)
 categories=''.join(f'<button class="category-chip" type="button" data-category="{c}" aria-pressed="false"><span>{j:02}</span>{h(names[c])}<small>8</small></button>' for j,(c,_,_) in enumerate(CATEGORIES,1))
 description=t('96 道 AI Agent 开发面试详解：模型基础、架构、RAG、MCP、记忆、规划、多 Agent、评测、安全、部署与项目追问。','96 detailed AI agent interview questions covering foundations, architecture, RAG, MCP, memory, planning, evaluation, security, production and project discussions.')
 title=t('AI Agent 开发面试题','AI Agent Interview Handbook')
 nav=''.join(f'<a href="./{f}{suffix}.html">{label}</a>' for f,label in [('index',t('开发手册','Handbook')),('practice',t('算法练习场','Coding practice')),('hot100',t('Hot 100 题解','Hot 100'))])
 schema={'@context':'https://schema.org','@type':'TechArticle','headline':title,'description':description,'inLanguage':'zh-CN' if zh else 'en','url':BASE+filename}
 html=f'''<!doctype html>
<html lang="{'zh-CN' if zh else 'en'}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{title} · Agent Fieldnotes</title><meta name="description" content="{h(description)}"><meta name="theme-color" content="#254c3c">
<link rel="canonical" href="{BASE+filename}"><link rel="alternate" hreflang="zh-CN" href="{BASE}interview.html"><link rel="alternate" hreflang="en" href="{BASE}interview-en.html"><link rel="alternate" hreflang="x-default" href="{BASE}interview.html"><link rel="stylesheet" href="./interview.css"><script type="application/ld+json">{json.dumps(schema,ensure_ascii=False)}</script><script src="./interview.js" defer></script><script src="./gold-watch-config.js?v=20261016" defer></script><script src="./gold-watch.js?v=20261016" defer></script></head>
<body><a class="skip" href="#reader">{t('跳到题解','Skip to answer')}</a><header class="site-header"><a class="brand" href="./index{suffix}.html"><b>A</b><span>Agent Fieldnotes</span></a><nav class="main-nav" aria-label="{t('主导航','Main navigation')}">{nav}<a href="./{filename}" aria-current="page">{t('Agent 面试','Agent interview')}</a></nav><nav class="language-switch" aria-label="Language / 语言"><a href="./interview.html?lang=zh" data-language="zh" aria-current="{'true' if zh else 'false'}" lang="zh-CN">中文</a><a href="./interview-en.html?lang=en" data-language="en" aria-current="{'false' if zh else 'true'}" lang="en">EN</a></nav></header>
<main><section class="hero"><div><p class="eyebrow">THE AGENT INTERVIEW HANDBOOK</p><h1>{t('把原理讲清楚，<br>把项目<span>讲完整。</span>','Explain the principles.<br><span>Own the engineering.</span>')}</h1><p class="lead">{t('从模型基础到生产落地，沿着问题、原理、实现与取舍，准备一场有深度的技术面试。','From model foundations to production systems: connect each answer to its mechanism, implementation and engineering trade-offs.')}</p></div><aside class="learning-card"><span class="eyebrow">YOUR LEARNING MAP</span><div class="stats"><div><strong>96</strong><span>{t('详解题目','Detailed answers')}</span></div><div><strong>12</strong><span>{t('知识模块','Knowledge areas')}</span></div></div><label for="study-progress">{t('我的掌握进度','My learning progress')}<b id="progress-label">0 / 96</b></label><progress id="study-progress" value="0" max="96">0 / 96</progress><p>{t('进度保存在当前浏览器，中英文共享。','Progress stays in this browser and is shared across languages.')}</p></aside></section>
<section class="module-section" aria-labelledby="modules-title"><div class="section-heading"><h2 id="modules-title">{t('按知识模块学习','Explore by knowledge area')}</h2><button id="show-all" type="button">{t('查看全部题目','View all questions')} ↗</button></div><div class="categories">{categories}</div></section>
<section class="workspace" id="questions"><aside class="catalog" aria-labelledby="catalog-title"><div class="catalog-head"><h2 id="catalog-title">{t('题目目录','Question index')}</h2><span id="result-count">96</span></div><label for="search">{t('搜索题目与答案','Search questions and answers')}</label><div class="search-wrap"><input id="search" type="search" placeholder="{t('例如：幂等、RAG、MCP','e.g. idempotency, RAG, MCP')}" autocomplete="off"><button id="clear-search" type="button" aria-label="{t('清空搜索','Clear search')}">×</button></div><label for="category">{t('知识模块','Knowledge area')}</label><select id="category"><option value="all">{t('全部模块','All areas')} · 96</option>{options}</select><label class="unread-filter"><input type="checkbox" id="unread-only">{t('仅看未掌握','Only not yet learned')}</label><nav class="question-list" aria-label="{t('面试题目录','Interview questions')}">{''.join(links)}</nav><p id="no-results" hidden>{t('没有匹配的题目，试试其他关键词或模块。','No matching questions. Try another keyword or area.')}</p></aside><div class="reader" id="reader">{''.join(articles)}</div></section>
<footer><p>{t('题目主题参考以下开源题库，答案按原理、实现和工程场景重新组织与独立编写。','Question topics draw on the following public repositories; explanations are independently written and organized around mechanisms, implementation and engineering scenarios.')}</p><a href="https://github.com/BigKunLun/Agent-Interview-100" target="_blank" rel="noopener noreferrer">Agent-Interview-100 ↗</a><a href="https://github.com/smile-struggler/kaomian" target="_blank" rel="noopener noreferrer">kaomian ↗</a><a href="https://github.com/leftagent/agent-fieldnotes" target="_blank" rel="noopener noreferrer">GitHub ↗</a></footer></main><div id="toast" role="status" aria-live="polite"></div><noscript><p class="noscript">{t('所有题解均可直接阅读。搜索与进度记录需要启用 JavaScript。','All answers remain readable. Search and progress tracking require JavaScript.')}</p></noscript></body></html>'''
 (ROOT/filename).write_text(html)
 print(filename,len(ordered),'questions')
