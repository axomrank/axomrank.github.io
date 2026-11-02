#!/usr/bin/env python3
"""One-time glossary and guide enrichment from explicitly authored unit facts.
Preserves existing entity keys and all published lesson/exercise ids.
"""
import csv,importlib,json,re,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT/'docs/authoring'))
def read(p):return json.loads(p.read_text())
def save(o,p):p.write_text(json.dumps(o,ensure_ascii=False,indent=1)+'\n')
def key(s):return re.sub(r'[^a-z0-9]+','-',s.lower()).strip('-')
E=read(ROOT/'content/entities.json');names={e['name']['en'].lower():k for k,e in E.items()};rows=list(csv.DictReader(open('/home/angsuman/extra_spac/Assam History/data/assam_history.csv',encoding='utf-8-sig')))
places={r['name'].lower():r for r in rows if r['type']=='place' and r['lat'] and r['lon']}
for mod,cid in [('early_new_units','early-assam'),('medieval_new_units','medieval-kingdoms'),('british_new_units','british-period'),('culture_units','assam-culture'),('heritage_units','heritage-and-sources'),('modern_units','modern-assam'),('peoples_units','peoples-councils-movements')]:
 briefs=importlib.import_module(mod).LESSONS;c=read(ROOT/f'content/courses/{cid}.json')
 for n,brief in briefs.items():
  row=next(r for r in c['kings'] if r['n']==n);p=ROOT/f"content/lessons/{row['lesson']}.json";l=read(p);timeline=l.setdefault('guide',{}).setdefault('timeline',[])
  for i,b in enumerate(brief['units']):
   if 'borrow' in b:continue
   u=l['units'][i]
   for f in b['facts']:
    if f[4]=='year' and re.fullmatch(r'\d{3,4}',f[2]):
     item={'y':f[2],'t':{'en':u['title']['en']+' · '+f[0],'as':u['title']['as']+' · '+f[1]},'unit':u['id']}
     if not any(x['y']==item['y'] and x['t']==item['t'] for x in timeline):timeline.append(item)
    if f[4] not in ['person','place','community','institution','work','term','office','language','title','award']:continue
    eid=names.get(f[2].lower()) or key(f[2])
    if not eid:continue
    if eid in E and E[eid]['name']['en'].lower()!=f[2].lower():eid='history-'+eid
    if eid not in E:
     E[eid]={'type':{'community':'people','institution':'term','work':'term','language':'term','title':'term','award':'term'}.get(f[4],f[4]),'name':{'en':f[2],'as':f[3]},'meaning':{'en':f[0]+' '+f[2]+'.','as':f[1]+' '+f[3]+'।'},'lessons':[],'sources':[{'lesson':l['id'],'unit':u['id']} ]}
     if f[2].lower() in places:
      r=places[f[2].lower()];E[eid]['geo']=[float(r['lat']),float(r['lon'])];E[eid]['geo_note']='Town-level orientation from the user-provided source library,not an exact event location.'
     names[f[2].lower()]=eid
    if l['id'] not in E[eid].setdefault('lessons',[]):E[eid]['lessons'].append(l['id'])
    # Link the first natural occurrence in the narrative,not answer options.
    for s in u['steps']:
     if s['type']!='story':continue
     linked=False
     for para in s['text']:
      if '[[' in para['en'] and eid in para['en']:linked=True;break
      if re.search(r'(?<![\w])'+re.escape(f[2])+r'(?![\w])',para['en']):
       para['en']=re.sub(r'(?<![\w])'+re.escape(f[2])+r'(?![\w])','[['+eid+'|'+f[2]+']]',para['en'],count=1)
       if f[3] in para['as']:para['as']=para['as'].replace(f[3],'[['+eid+'|'+f[3]+']]',1)
       linked=True;break
     if linked:break
   # Meaningful prior-unit continuity:explicitly point to the preceding taught unit.
   if i and not any(s.get('link') for s in u['steps'] if s['type']=='story'):
    next(s for s in u['steps'] if s['type']=='story')['link']={'unit':l['units'][i-1]['id'],'note':{'en':'Build on the preceding unit: '+l['units'][i-1]['title']['en'],'as':'আগৰ অধ্যায়ৰ পৰা আগবাঢ়া: '+l['units'][i-1]['title']['as']}}
  save(l,p)
save(E,ROOT/'content/entities.json');print('Glossary:',len(E),'entities;source-based guides and narrative links added')
