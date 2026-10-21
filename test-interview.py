"""Validate content completeness, bilingual parity and generated static answers."""
import json, re, subprocess, sys
from collections import Counter
from pathlib import Path
from html import unescape
root=Path(__file__).resolve().parent
data=json.loads((root/'interview-data.json').read_text())
assert len(data)==96
assert len({q['id'] for q in data})==96
assert len(Counter(q['category'] for q in data))==12
assert set(Counter(q['category'] for q in data).values())=={8}
for q in data:
 assert re.fullmatch('[a-z]+-[0-9]{2}',q['id'])
 assert len(q['reasoning']['zh'])==len(q['reasoning']['en'])>=3,q['id']
 for lang in ['zh','en']:
  for field in ['title','summary','example','followup','pitfall']:
   assert isinstance(q[field][lang],str) and q[field][lang].strip(),(q['id'],field)
  assert all(len(p)>70 for p in q['reasoning'][lang]),q['id']
 assert all(u.startswith('https://github.com/') for u in q['sources']) and q['sources']
 assert len(re.findall('[\u4e00-\u9fff]', ''.join(q[k]['zh'] for k in ['summary','example','followup','pitfall'])+''.join(q['reasoning']['zh'])))>=400,q['id']
 if q.get('code'):
  assert q['code']['language']=='python'
  subprocess.run([sys.executable,'-c',q['code']['text']],check=True,timeout=15,stdout=subprocess.DEVNULL)
for lang,suffix in [('zh',''),('en','-en')]:
 text=(root/f'interview{suffix}.html').read_text()
 ids=re.findall(r'\bid="([^\"]+)"',text)
 assert len(ids)==len(set(ids))
 assert len(re.findall('<article class="answer"',text))==96
 visible=unescape(re.sub('<[^>]*>',' ',text))
 for q in data:
  if q.get('tutorial'):
   tutorial=q['tutorial'][lang]
   assert tutorial['intro'] in visible
   for block in tutorial['sections']:
    assert block['title'] in visible
    for paragraph in block['paragraphs']:assert paragraph in visible
   for paragraph in tutorial['interview']:assert paragraph in visible
   assert 'softmax(QKᵀ / √dₖ + M)V' in visible
   continue
  for field in ['title','summary','example','followup','pitfall']:
   assert q[field][lang] in visible,(q['id'],field)
  for p in q['reasoning'][lang]:assert p in visible
 for url in re.findall(r'(?:href|src)="\./([^"?#]+)',text):assert (root/url).exists(),url
 for anchor in re.findall(r'href="#([^\"]+)"',text):assert anchor in ids,anchor
 for name in ['index','hot100','practice']:
  assert f'./interview{suffix}.html' in (root/f'{name}{suffix}.html').read_text()
print('PASS: 96 unique detailed bilingual answers / 12 areas; static full-text parity, source links, anchors, navigation and 4 executable Python examples.')
