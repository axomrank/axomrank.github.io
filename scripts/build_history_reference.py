#!/usr/bin/env python3
"""Build the public cross-course reference only from integrated content."""
import json,re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def read(p):return json.loads(p.read_text())
courses={c['id']:c for p in (ROOT/'content/courses').glob('*.json') if (c:=read(p))};lessons={l['id']:l for p in (ROOT/'content/lessons').glob('*.json') if (l:=read(p))};E=read(ROOT/'content/entities.json');used={k:set(e.get('lessons',[]))&lessons.keys() for k,e in E.items()};events=[];seen=set()
for lid,l in lessons.items():
 for eid in re.findall(r'\[\[([^|\]]+)',json.dumps(l['units'],ensure_ascii=False)):
  if eid in used:used[eid].add(lid)
 for item in l.get('guide',{}).get('timeline',[]):
  y=str(item.get('y',''));m=re.search(r'\d{3,4}',y)
  if not m:continue
  sig=(l.get('course','ahom-kings'),y,item['t']['en'])
  if sig in seen:continue
  seen.add(sig);events.append({'year':int(m[0]),'date':y,'title':item['t'],'lesson':lid,'course':l.get('course','ahom-kings'),'unit':item.get('unit')})
refs={'courses':[{'id':c['id'],'title':c['title'],'optional':c['id']=='ahom-kings'} for c in sorted(courses.values(),key=lambda c:c.get('order',0))], 'lessons':{lid:{'title':l['king'],'course':l.get('course','ahom-kings'),'period':l['reign']} for lid,l in lessons.items()},'events':sorted(events,key=lambda e:(e['year'],e['lesson'])), 'entities':[{'id':eid,'type':e['type'],'name':e['name'],'meaning':e['meaning'],'lessons':sorted(used[eid]),**({'geo':e['geo']} if e.get('geo') else {})} for eid,e in E.items() if used[eid]]}
p=ROOT/'content/history-reference.json';p.write_text(json.dumps(refs,ensure_ascii=False,indent=1)+'\n');print('History reference:',len(refs['events']),'dated entries;',len(refs['entities']),'linked names')
if __name__=='__main__':pass
