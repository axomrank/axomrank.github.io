#!/usr/bin/env python3
"""One-time consolidation, retaining lesson, exercise and checkpoint ids."""
import copy,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
def read(p):return json.loads(p.read_text())
def save(o,p):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(o,ensure_ascii=False,indent=1)+'\n')
def B(e,a):return {'en':e,'as':a}
out=ROOT/'content/courses/assam-history.json'
if out.exists():raise SystemExit('Already consolidated;edit the unified course without regenerating ids.')
source_ids=['early-assam','varman-kings','salastambha-kings','pala-kings','medieval-kingdoms','ahom-kingdom','british-period','modern-assam','assam-culture','heritage-and-sources','peoples-councils-movements']
sources={cid:read(ROOT/f'content/courses/{cid}.json') for cid in source_ids}
# Foundations,then the dynasties,then the transition out of Kamarupa.
ordered=[]
def take(cid,predicate=lambda row:True):
 for row in sources[cid]['kings']:
  if predicate(row):ordered.append((cid,row))
take('early-assam',lambda row:row['n']<=3)
for cid in ['varman-kings','salastambha-kings','pala-kings']:take(cid)
take('early-assam',lambda row:row['n']==4)
for cid in source_ids[4:]:take(cid)
assert len(ordered)==93
course={'id':'assam-history','order':1,'title':B('Assam History','অসমৰ ইতিহাস'),'eyebrow':B('One continuous learning path','এটা অবিচ্ছিন্ন শিক্ষাৰ পথ'),'subtitle':B('93 lessons ·380 units ·checkpoints along the way','৯৩টা পাঠ ·৩৮০টা অধ্যায় ·মাজে মাজে পুনৰীক্ষণ'),'tabs':['lessons','profile'],'bank':'content/questions/assam-history.json','kings':[],'eras':[]}
positions={};lessons={}
for n,(cid,row) in enumerate(ordered,1):
 row=copy.deepcopy(row);row['n']=n;course['kings'].append(row);positions[row['lesson']]=n
 p=ROOT/f"content/lessons/{row['lesson']}.json";l=read(p);l['origin_course']=cid;l['origin_no']=l['no'];l['course']='assam-history';l['no']=n;lessons[l['id']]=l
for cid,c in sources.items():
 for era in c['eras']:
  included=[positions[r['lesson']] for r in c['kings'] if era['from']<=r['n']<=era['to']]
  assert included and sorted(included)==list(range(min(included),max(included)+1))
  e=copy.deepcopy(era);e.update({'from':min(included),'to':max(included),'origin_course':cid});course['eras'].append(e)
course['eras'].sort(key=lambda e:e['from']);assert len({e['id']for e in course['eras']})==len(course['eras'])
assert sorted(n for e in course['eras'] for n in range(e['from'],e['to']+1))==list(range(1,94))
bank={'note':'Unified Assam History practice.All original question ids,lesson references and checkpoint era ids are preserved.','questions':[]}
for cid,c in sources.items():
 cp=ROOT/f'content/courses/{cid}.json';bp=ROOT/c['bank']
 save(c,ROOT/f'docs/authoring/pre-unification/courses/{cp.name}')
 old=read(bp);save(old,ROOT/f'docs/authoring/pre-unification/questions/{bp.name}');bank['questions']+=old['questions']
 cp.unlink();bp.unlink()
for lid,l in lessons.items():save(l,ROOT/f'content/lessons/{lid}.json')
# Cross-lesson callouts display the new global lesson number.
for p in (ROOT/'content/lessons').glob('*.json'):
 l=read(p);dirty=False
 for u in l['units']+[l['test']]:
  for step in u['steps']:
   link=step.get('link',{})
   if link.get('lessonId')in positions and link.get('lesson'):
    link['lesson']=positions[link['lessonId']];dirty=True
 if dirty:save(l,p)
save(course,out);save(bank,ROOT/course['bank'])
# Keep the original optional deep-dive endpoints for existing saved links only.
legacy=ROOT/'content/courses/ahom-kings.json';c=read(legacy);c['archived']=True;c['redirect_to']='assam-history';save(c,legacy)
cat=read(ROOT/'content/catalog.json');s=next(s for s in cat['subjects'] if s['id']=='assam-history');s['courses']=[{'course':'assam-history'}];cat['course_redirects']={cid:'assam-history' for cid in source_ids+['ahom-kings']};save(cat,ROOT/'content/catalog.json')
save({'date':'2026-11-02','course':'assam-history','lesson_count':len(ordered),'units':380,'questions':len(bank['questions']),'checkpoints':len(course['eras']),'mapping':[{'lesson':row['lesson'],'origin_course':cid,'no':n}for n,(cid,row)in enumerate(ordered,1)],'compatibility':'Permanent lesson,unit,exercise,question and era ids retained.No reset of saved progress.'},ROOT/'docs/research/history-unification.json')
print('Unified93lessons,380units,',len(bank['questions']),'questions,',len(course['eras']),'checkpoints')
