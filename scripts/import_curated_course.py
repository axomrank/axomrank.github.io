#!/usr/bin/env python3
"""Import a new course once, preserving ids on subsequent editorial changes.

Usage: import_curated_course.py docs/authoring/NAME.json
The configuration points to explicit bilingual briefs and a source register.
"""
import copy,csv,hashlib,importlib.util,json,shutil,sys
from pathlib import Path
from compile_history_units import compile_unit,bank_questions
from lesson_authoring import bi as B,identify,new_test
ROOT=Path(__file__).resolve().parents[1];LIB=Path('/home/angsuman/extra_spac/Assam History');sys.path.insert(0,str(ROOT/'docs/authoring'))
def read(p):return json.loads(Path(p).read_text())
def save(o,p):Path(p).parent.mkdir(parents=True,exist_ok=True);Path(p).write_text(json.dumps(o,ensure_ascii=False,indent=1)+'\n')
def import_course(config):
 cfg=read(ROOT/config);C=cfg['course'];CID=C['id'];out=ROOT/f'content/courses/{CID}.json'
 if out.exists():raise ValueError('Course exists. Edit JSON without regenerating published ids: '+CID)
 spec=importlib.util.spec_from_file_location('curated_'+CID,ROOT/cfg['briefs']);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);briefs=m.LESSONS
 sources=cfg['sources'];assets=[];rows={r['id']:r for r in csv.DictReader(open(LIB/'data/assam_history.csv',encoding='utf-8-sig'))}
 def asset(sid):
  row=rows[sid];src=LIB/row['scene_image'];target=ROOT/f'content/media/{CID}/{sid.lower()}.webp';target.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(src,target);rel=f'{CID}/{target.name}'
  if not any(a['file']==rel for a in assets):assets.append({'file':rel,'source_record':sid,'source_file':row['scene_image'],'kind':'modern artistic reconstruction','sha256':hashlib.sha256(src.read_bytes()).hexdigest()})
  return rel
 pools={}
 for l in briefs.values():
  for u in l['units']:
   for f in u.get('facts',[]):
    if B(f[2],f[3]) not in pools.setdefault(f[4],[]):pools[f[4]].append(B(f[2],f[3]))
 for kind,vals in cfg.get('distractors',{}).items():
  for pair in vals:
   if B(*pair) not in pools.setdefault(kind,[]):pools[kind].append(B(*pair))
 lessons=[];bank={'note':'Original source-linked practice questions; no previous-year-paper provenance claimed.','questions':[]};C.setdefault('tabs',['lessons','profile']);C['bank']=f'content/questions/{CID}.json';C['kings']=[]
 for n in sorted(set(briefs)|set(map(int,cfg.get('drafts',{})))):
  if str(n) in cfg.get('drafts',{}):
   L=read(ROOT/cfg['drafts'][str(n)]);L['course']=CID;L['no']=n
  else:
   brief=briefs[n];lid=brief.get('id',f'{CID}-{n:02}');units=[];refs=[sources[k] for k in brief['source_keys']];shows=['brahmaputra','guwahati','jorhat','sadiya','dimapur'];mapping={'box':[88.5,23,97,29],'show':shows}
   for i,u in enumerate(brief['units'],1):
    if 'borrow' in u:
     src=read(ROOT/f"content/lessons/{u['borrow']['lesson']}.json");unit=copy.deepcopy(next(x for x in src['units'] if x['id']==u['borrow']['unit']));unit['id']=f'u{i}';unit['title']=B(*u['title']);unit['steps']=[s for s in unit['steps'] if s['type']!='mcq'];unit['steps'].sort(key=lambda s:s['type']!='story')
     for s in unit['steps']:
      s.pop('id',None)
      if s.get('img') and '/' not in s['img']:s['img']=src['id']+'/'+s['img']
      if s['type']=='picture':s['options']=[x if '/' in x else src['id']+'/'+x for x in s['options']]
      if s['type']=='map':s.setdefault('map',src['map']);shows.extend(s['choices'])
      if s.get('link') and 'lessonId' not in s['link']:s['link']['lessonId']=src['id']
     unit['steps']+=copy.deepcopy(u.get('extra',[]))
     refs+=src['sources'];unit['adapted_from']={'lesson':src['id'],'unit':u['borrow']['unit']};units.append(unit)
    else:
     for c in u['cards']:
      if c.get('scene'):c['img']=asset(c.pop('scene'))
     unit=compile_unit(u,pools,lid+'.'+u['id']);units.append(unit)
     for s in unit['steps']:
      if s['type']=='map':shows.extend(s['choices'])
   mapping['show']=list(dict.fromkeys(shows))
   portrait=next((s['img'] for u in units for s in u['steps'] if s.get('img')),cfg.get('fallback_portrait','british-period/frontier-map.webp'))
   L={'id':lid,'course':CID,'no':n,'version':1,'eyebrow':C['eyebrow'],'king':B(*brief['title']),'reign':B(*brief['span']),'portrait':portrait,'map':mapping,'guide':{'timeline':[]},'sources':list({json.dumps(r,sort_keys=True):r for r in refs}.values()),'units':units,'test':new_test([s for u in units for s in [x for x in u['steps'] if x['type']!='story'][:2]]),'review_notes':'AI-assisted bilingual educational content. Source and uncertainty notes retained. Fluent Assamese educator review remains pending. Illustrations are interpretive; adapted units carry new permanent ids.'}
   identify(L,lid)
   era=next(e['id'] for e in C['eras'] if e['from']<=n<=e['to']);bank['questions']+=bank_questions(L,[u for u in brief['units'] if 'borrow' not in u],pools,era)
  lessons.append(L)
  C['kings'].append({'n':n,'id':L['id'],'lesson':L['id'],'name':L['king'],'reign':L['reign']['en'],'face':L['portrait'],'tier':'A' if len(L['units'])>=6 else 'B' if len(L['units'])>=4 else 'C','rel':{'type':'other','of':None,'t':B('','')}})
  # Fresh questions for adapted units and private drafts, from explicit keys.
  era=next(e['id'] for e in C['eras'] if e['from']<=n<=e['to'])
  for u in L['units']:
   if n in briefs and not next((b for b in briefs[n]['units'] if b['id']==u['id']),{}).get('borrow'):continue
   for i,s in enumerate(u['steps']):
    if s['type'] not in ('tf','whoami','inline'):continue
    q={'id':f"bank.{L['id']}.{u['id']}.{i:02}",'type':'mcq','era':era,'lesson':L['id'],'difficulty':'easy','exams':['ADRE','APSC','TET','SI'],'why':s['why']}
    if s['type']=='tf':q.update(q=s['s'],options=[B('True','শুদ্ধ'),B('False','অশুদ্ধ')],answer=0 if s['answer'] else 1)
    elif s['type']=='whoami':q.update(q=B(' · '.join(x['en'] for x in s['clues']),' · '.join(x['as'] for x in s['clues'])),options=s['options'],answer=s['answer'])
    else:q.update(q=B(s['before']['en']+' …',s['before']['as']+' …'),options=s['options'],answer=s['answer'])
    bank['questions'].append(q)
 for L in lessons:save(L,ROOT/f"content/lessons/{L['id']}.json")
 save(C,out);save(bank,ROOT/C['bank']);save({'date':'2026-11-02','sources':sources},ROOT/f'docs/research/{CID}-sources.json');save({'source_library':str(LIB),'assets':assets,'rights':'User-authorised reuse; source content licence retained. Artistic reconstructions are not evidence.'},ROOT/f'docs/research/{CID}-assets.json')
 cat=read(ROOT/'content/catalog.json');sub=next(s for s in cat['subjects'] if s['id']=='assam-history');slot=cfg.get('catalog_slot')
 if slot:
  index=next(i for i,r in enumerate(sub['courses']) if r.get('soon') and slot.lower() in r['title']['en'].lower());sub['courses'][index]={'course':CID}
 else:sub['courses'].insert(cfg.get('catalog_position',len(sub['courses'])),{'course':CID})
 save(cat,ROOT/'content/catalog.json');print(CID,len(lessons),'lessons',sum(len(l['units']) for l in lessons),'units',len(bank['questions']),'questions')
if __name__=='__main__':import_course(sys.argv[1])
