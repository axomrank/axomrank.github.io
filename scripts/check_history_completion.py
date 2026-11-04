#!/usr/bin/env python3
"""Verify the delivered history scope and cross-course reference independently."""
import json,re,subprocess,sys
from pathlib import Path
from audit_lessons import audit
ROOT=Path(__file__).resolve().parents[1]
def read(p):return json.loads(p.read_text())
expected={'varman-kings':(3,19),'salastambha-kings':(3,12),'pala-kings':(3,14),'early-assam':(4,15),'medieval-kingdoms':(9,35),'ahom-kingdom':(15,63),'british-period':(18,75),'modern-assam':(11,42),'assam-culture':(13,55),'heritage-and-sources':(6,22),'peoples-councils-movements':(8,30),'ahom-kings':(41,152)}
ls={l['id']:l for p in (ROOT/'content/lessons').glob('*.json') if(l:=read(p))};entities=read(ROOT/'content/entities.json');steps={s['id'] for l in ls.values() for u in l['units']+[l['test']] for s in u['steps']};issues=[];core=units=questions=0
unified=read(ROOT/'content/courses/assam-history.json')
assert len(unified['kings'])==93
assert [row['n'] for row in unified['kings']]==list(range(1,94))
assert sorted(n for e in unified['eras'] for n in range(e['from'],e['to']+1))==list(range(1,94))
for cid,target in expected.items():
 mine=[l for l in ls.values() if l.get('origin_course',l.get('course','ahom-kings'))==cid]
 actual=(len(mine),sum(len(l['units']) for l in mine));assert actual==target,(cid,actual,target)
 for l in mine:
  if cid!='ahom-kings':
   assert l['course']=='assam-history';core+=1;units+=len(l['units']);issues+=audit(ROOT/f"content/lessons/{l['id']}.json")
  text=json.dumps(l['units'],ensure_ascii=False)
  assert not re.search(r'\[\[[^\]]*\[\[',text),('Nested name link',l['id'])
for cp in (ROOT/'content/courses').glob('*.json'):
 c=read(cp);bank=read(ROOT/c['bank']);questions+=len(bank['questions'])
 for q in bank['questions']:
  assert set(q.get('exams',[]))<= {'adre','tet','apsc','si'},('Unknown exam',q['id'])
  assert all(o.get('en') and o.get('as') for o in q['options']),q['id']
  if q.get('source_step'):assert q['source_step'] in steps,('Unknown source step',q['id'])
  assert len({o['en'].strip().lower() for o in q['options']})==len(q['options']),('Duplicate choices',q['id'])
assert not issues,'\n'.join(issues)
assert core==93 and units==382,(core,units)
assert questions>=2500,questions
cat=read(ROOT/'content/catalog.json');subject=next(s for s in cat['subjects'] if s['id']=='assam-history');assert subject['courses']==[{'course':'assam-history'}]
r=read(ROOT/'content/history-reference.json');assert set(r['lessons'])=={lid for lid,l in ls.items() if l.get('course')!='indian-constitution'}
for event in r['events']:assert event['lesson']in ls
for item in r['entities']:assert item['id']in entities and all(lid in ls for lid in item['lessons'])
# Existing saved references remain present,including story ids moved into extra guide context.
def ids(o):
 if isinstance(o,dict):
  out={o['id']} if isinstance(o.get('id'),str) else set()
  for value in o.values():out|=ids(value)
  return out
 if isinstance(o,list):return set().union(*(ids(x) for x in o)) if o else set()
 return set()
tracked=subprocess.run(['git','ls-files','content/lessons'],cwd=ROOT,capture_output=True,text=True,check=True).stdout.splitlines()
for file in tracked:
 old=subprocess.run(['git','show','HEAD:'+file],cwd=ROOT,capture_output=True,text=True)
 if old.returncode==0:assert ids(json.loads(old.stdout))<=ids(read(ROOT/file)),('Lost permanent ids',file)
print(f'History scope passed:{core}core lessons/{units}units;41optional lessons/152units;{questions}questions;{len(r["events"])}timeline entries;{len(r["entities"])}linked names;existing ids preserved.')
