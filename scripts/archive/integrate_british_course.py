#!/usr/bin/env python3
"""Integrate the authored British course; refuses to overwrite an existing release.

Run once per new authoring import. Subsequent edits belong in lesson JSON so
published exercise ids cannot accidentally be regenerated.
"""
import copy,csv,hashlib,importlib.util,json,re,shutil,sys
from pathlib import Path
from PIL import Image,ImageDraw
from compile_history_units import compile_lesson,bank_questions
from lesson_authoring import bi as B,match,inline,tf,who,map_question
ROOT=Path(__file__).resolve().parents[2]
LIB=Path('/home/angsuman/extra_spac/Assam History')
def read(p):return json.loads(Path(p).read_text())
def save(o,p):Path(p).parent.mkdir(parents=True,exist_ok=True);Path(p).write_text(json.dumps(o,ensure_ascii=False,indent=1)+'\n')
spec=importlib.util.spec_from_file_location('british_briefs',ROOT/'docs/authoring/british_new_units.py');module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
briefs=module.LESSONS
sources=read(ROOT/'docs/authoring/british_sources.json')
rows={r['id']:r for r in csv.DictReader(open(LIB/'data/assam_history.csv',encoding='utf-8-sig'))}
C=read(ROOT/'private/drafts/british-period/course.json');CID=C['id']
if (ROOT/f'content/courses/{CID}.json').exists():raise SystemExit('Course already integrated. Edit the existing JSON; do not regenerate permanent ids.')
assets=[]
def asset(sid):
 row=rows[sid];src=LIB/row['scene_image'];target=ROOT/f'content/media/british-period/{sid.lower()}.webp';target.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(src,target)
 rel=f'british-period/{target.name}'
 if not any(a['file']==rel for a in assets):assets.append({'file':rel,'source_record':sid,'source_file':row['scene_image'],'kind':'modern artistic reconstruction','sha256':hashlib.sha256(src.read_bytes()).hexdigest()})
 return rel
# A native location diagram is used where the library has no matching scene.
BASE=read(ROOT/'content/maps/assam.json');im=Image.new('RGB',(720,480),'#f4eddf');draw=ImageDraw.Draw(im)
west,south,east,north=89.5,24,96.6,28.6
project=lambda p:((p[1]-west)/(east-west)*680+20,(north-p[0])/(north-south)*440+20)
for r in BASE['rivers'].values():
 pts=[project(p) for p in r['pts']]
 if len(pts)>1:draw.line(pts,fill='#7b9aa4',width=3)
for lat,lon in [(26.18,91.75),(25.65,91.66),(25.28,91.73),(27.83,95.67)]:
 x,y=project([lat,lon]);draw.ellipse((x-7,y-7,x+7,y+7),fill='#b85535')
mp=ROOT/'content/media/british-period/frontier-map.webp';mp.parent.mkdir(parents=True,exist_ok=True);im.save(mp,'WEBP',quality=84)
assets.append({'file':'british-period/frontier-map.webp','kind':'native location diagram','source':'content/maps/assam.json; modern orientation only, no historical sovereignty boundary','sha256':hashlib.sha256(mp.read_bytes()).hexdigest()})
# Explicit fact pools provide grammatical-category distractors across this course.
pools={}
for lesson in briefs.values():
 for u in lesson['units']:
  for f in u['facts']:
   pools.setdefault(f[4],[])
   x=B(f[2],f[3])
   if x not in pools[f[4]]:pools[f[4]].append(x)
seeds={'office':[('Borphukan','বৰফুকন'),('Burhagohain','বুঢ়াগোহাঁই')],
 'language':[('English','ইংৰাজী'),('Sanskrit','সংস্কৃত')],
 'title':[('Kalaguru','কলাগুৰু'),('Rupkonwar','ৰূপকোঁৱৰ'),('Lokapriya','লোকপ্ৰিয়')],
 'number':[('17','১৭'),('39','৩৯'),('150','১৫০')],
 'month':[('April','এপ্ৰিল'),('August','আগষ্ট'),('June','জুন')],
 'community':[('Koch','কোচ'),('Dimasa','ডিমাছা'),('Ahom','আহোম')],
 'community_group':[('Koch, Ahom and Chutia','কোচ, আহোম আৰু চুতীয়া'),('Khasi, Pnar and Garo','খাচী, পনাৰ আৰু গাৰো'),('Khamti, Singpho and Naga','খামতি, চিংফৌ আৰু নগা')],
 'country':[('Britain','ব্ৰিটেইন')],
 'group':[('Teachers','শিক্ষকসকল'),('Soldiers','সৈনিকসকল')],
 'work':[('Hemkosh','হেমকোষ'),('Harshacharita','হৰ্ষচৰিত')],
 'event':[('First Anglo-Burmese War','প্ৰথম ইংগ-বৰ্মী যুদ্ধ'),('Treaty of Yandabo','ইয়াণ্ডাবু সন্ধি'),('Dandi March','দাণ্ডি যাত্ৰা')]}
for kind,vals in seeds.items():
 for en,ass in vals:
  if B(en,ass) not in pools.setdefault(kind,[]):pools[kind].append(B(en,ass))
ENT=read(ROOT/'content/entities.json')
for k,v in read(ROOT/'private/drafts/british-period/entities.json').items():
 if k in ENT and ENT[k]!=v:raise ValueError(f'Entity conflict: {k}')
 ENT[k]=v
# Town-level locations from the source library, not alleged exact battle positions.
for key,ass in [('phulaguri','ফুলগুৰি'),('patharughat','পথৰুঘাট'),('gohpur','গহপুৰ'),('kohima','কহিমা'),('imphal','ইম্ফল'),('ledo','লিডু')]:
 r=rows[key];ENT.setdefault(key,{'type':'place','name':B(r['name'],ass),'meaning':B(r['summary'],f"{ass}: এই পাঠৰ সৈতে জড়িত ঐতিহাসিক ঠাই"),'geo':[float(r['lat']),float(r['lon'])],'sources':[s for s in r['sources'].split('; ') if s],'geo_note':'Town-level orientation from user source library; not an exact event-site coordinate.'})
# Attach explicit map exercises to place facts, preserving the authored main interaction.
map_briefs={ (5,0):('phulaguri','Tap Phulaguri, the site of the 1861 rising.','১৮৬১ৰ বিদ্ৰোহৰ ঠাই ফুলগুৰি টিপা।'),(6,3):('patharughat','Tap Patharughat in Darrang.','দৰঙৰ পথৰুঘাট টিপা।'),(11,1):('guwahati','Tap Guwahati, the Chhatra Sanmilan’s first meeting place.','ছাত্ৰ সন্মিলনৰ প্ৰথম সভাৰ ঠাই গুৱাহাটী টিপা।'),(15,1):('gohpur','Tap Gohpur, associated with Kanaklata’s procession.','কনকলতাৰ শোভাযাত্ৰাৰ ঠাই গহপুৰ টিপা।'),(16,1):('kohima','Tap Kohima, one of the 1944 battle sites.','১৯৪৪ৰ যুদ্ধৰ এটা ঠাই কহিমা টিপা।'),(16,2):('ledo','Tap Ledo, the road’s starting point in Assam.','অসমত পথটোৰ আৰম্ভণিৰ ঠাই লিডু টিপা।'),(18,0):('sylhet','Tap Sylhet, where the 1947 referendum was held.','১৯৪৭ৰ গণভোটৰ ঠাই শ্ৰীহট্ট টিপা।')}
for (number,index),(target,q,ass) in map_briefs.items():
 choices=[target]+[x for x in ['guwahati','jorhat','sivasagar','nagaon'] if x!=target][:3]
 briefs[number]['units'][index]['extra']=map_question(B(q,ass),target,choices,B('Use the location with the event and date taught in this unit.','এই অধ্যায়ত শিকা ঘটনা আৰু চনৰ সৈতে ঠাইটো মিলোৱা।'))
# Resolve selected library illustrations. Their visual details remain interpretive.
for lesson in briefs.values():
 for u in lesson['units']:
  for card in u['cards']:
   if card.get('scene'):card['img']=asset(card.pop('scene'))
# Correct source notes as additional records were consulted.
sources['ledo']={'title':'Changlang district: Stilwell Road (Ledo Road)','url':'https://changlang.nic.in/stilwell-road-ledo-road/','used_for':'Ledo–Burma–China route, Kunming connection and General Joseph Stilwell; no disputed exact opening date taught.'}
sources['dictionary']['url']='https://openlibrary.org/books/OL7027960M/A_dictionary_in_Assamese_and_English';sources['dictionary']['used_for']='1867 Bronson dictionary bibliographic record; Hemkosh 1900 cross-checked with the IIT Guwahati-associated catalogue. Assamese editorial review remains pending.'
sources['bezbaroa']={'title':'IIT Guwahati Board of Governors, meeting 78, item 21/2014','url':'https://www.iitg.ac.in/pdf/591078BOG_PDFOG_PDF.pdf','used_for':'Rasaraj for humorous/satirical writing and Kripabar persona; works corroborated by Kalakshetra museum catalogue.'}
# Metadata and bank integration.
bank=read(ROOT/'private/drafts/british-period/questions.json');all_lessons=[]
def era_for(n):return next(e['id'] for e in C['eras'] if e['from']<=n<=e['to'])
for number,brief in sorted(briefs.items()):
 lid=C['kings'][number-1]['id'];title=B(*brief['title']);units=brief['units']
 portrait=next((c['img'] for u in units for c in u['cards'] if c.get('img')),'british-period/frontier-map.webp')
 shows=['brahmaputra','guwahati','jorhat','sivasagar','nagaon']
 for u in units:
  if u.get('extra',{}).get('type')=='map':shows.extend(u['extra']['choices'])
 meta={'id':lid,'course':CID,'no':number,'version':1,'eyebrow':B('Assam History · British period','অসমৰ ইতিহাস · ব্ৰিটিছ যুগ'),'king':title,'reign':B(*brief['span']),'portrait':portrait,
       'sources':[sources[k] for k in brief['source_keys']],
       'review_notes':'Original AI-assisted bilingual draft, 2026-11-02. Sources and uncertainty notes retained. Fluent Assamese educator review has not occurred; no past-paper provenance is claimed. Illustration details are interpretive.',
       'map':{'box':[89.8,23.7,96.4,28.5],'show':list(dict.fromkeys(shows))},
       'guide':{'timeline':[]}}
 if number>4:
  prev=C['kings'][number-2];units[0]['cards'][0]['link']={'lessonId':prev['id'],'lesson':number-1,'unitNo':1,'unitTitle':prev['name'],'note':B('Continue the connected economic, cultural or political history of colonial Assam.','ঔপনিৱেশিক অসমৰ সম্পৰ্কিত অৰ্থনৈতিক, সাংস্কৃতিক বা ৰাজনৈতিক ইতিহাস আগবঢ়োৱা।')}
 L=compile_lesson(meta,units,pools)
 # Guide timeline is based on explicitly taught year facts, not invented dates.
 seen=set()
 for u in units:
  for f in u['facts']:
   if f[4]=='year' and (f[2],f[0]) not in seen:
    L['guide']['timeline'].append({'y':f[2],'t':B(f[0],f[1])});seen.add((f[2],f[0]))
 all_lessons.append(L);bank['questions'].extend(bank_questions(L,units,pools,era_for(number)))
 C['kings'][number-1].update({'lesson':lid,'face':portrait,'name':title,'reign':brief['span'][0]})
# Existing drafts are imported intact before targeted editorial corrections.
for p in sorted((ROOT/'private/drafts/british-period/lessons').glob('*.json')):
 L=read(p);n=L['no'];L['portrait']=asset('AHOM-228') if n==1 else 'british-period/frontier-map.webp' if n==2 else asset('COL-04')
 # Copy only relevant existing body images if any; symbolic art/map cards remain native.
 for u in L['units']+[L['test']]:
  for s in u['steps']:
   if s.get('img'):
    s['img']=s['img'] if '/' in s['img'] else f"{L['id']}/{s['img']}"
 if n==1:
  L['units'][0]['steps'][2]['text'][1]=B('The Company expanded its control after the treaty. Lower and Upper Assam did not pass through identical arrangements.','সন্ধিৰ পিছত কোম্পানীয়ে নিয়ন্ত্ৰণ বঢ়ায়। নামনি আৰু উজনি অসমৰ ব্যৱস্থা হুবহু একে নাছিল।')
  L['units'][2]['steps'][0]['text'][0]=B('Later, Francis Jenkins served as Commissioner of Assam from 1834 to 1861.','পিছলৈ ফ্ৰান্সিছ জেংকিন্সে ১৮৩৪ৰ পৰা ১৮৬১লৈ অসমৰ কমিচনাৰ হিচাপে কাম কৰে।')
  old=L['units'][0]['steps'][1];new=who([B('I fought the British in the war beginning in 1824.','১৮২৪ত আৰম্ভ হোৱা যুদ্ধত মই ব্ৰিটিছৰ বিৰুদ্ধে যুঁজিছিলোঁ।'),B('I gave up claims to Assam at Yandabo.','ইয়াণ্ডাবুত অসমৰ দাবী এৰিছিলোঁ।'),B('My historical name here is Burma.','ইয়াত মোৰ ঐতিহাসিক নাম বাৰ্মা।')],[B('Burma','বাৰ্মা'),B('Bhutan','ভূটান'),B('Nepal','নেপাল')],0,B('The First Anglo-Burmese War was between the British and Burma.','প্ৰথম ইংগ-বৰ্মী যুদ্ধ ব্ৰিটিছ আৰু বাৰ্মাৰ মাজত হৈছিল।'));new['id']=old['id'];L['units'][0]['steps'][1]=new
  old=L['units'][2]['steps'][-1];new={'type':'timeline','id':old['id'],'anchors':[{'y':'1836','l':B('Bengali policy','বাংলা ভাষাৰ নীতি')},{'y':'1874','l':B('Separate Assam','পৃথক অসম')}],'items':[{'t':B('Yandabo, 1826','ইয়াণ্ডাবু, ১৮২৬'),'slot':0},{'t':B('Restoration convention, 1873','পুনৰ্প্ৰতিষ্ঠাৰ প্ৰচলিত চন, ১৮৭৩'),'slot':1},{'t':B('Jonaki, 1889','জোনাকী, ১৮৮৯'),'slot':2}],'why':B('1826 → 1836 → 1873 → 1874 → 1889.','১৮২৬ → ১৮৩৬ → ১৮৭৩ → ১৮৭৪ → ১৮৮৯।')};L['units'][2]['steps'][-1]=new
 if n==2:
  # Sources differ on the day of the Khamti attack; teach January and year only.
  raw=json.dumps(L,ensure_ascii=False).replace('28 January 1839','January 1839').replace('১৮৩৯ চনৰ ২৮ জানুৱাৰীত','১৮৩৯ চনৰ জানুৱাৰীত')
  L=json.loads(raw);L['sources'].append({'title':'Eastern West Khasi Hills district: U Tirot Singh memorial','url':'https://easternwestkhasihills.meghalaya.gov.in/culture-heritage/','used_for':'Nongkhlaw resistance, January 1833 imprisonment and death at Dhaka in 1835.'})
 if n==3:
  # Omit disputed petition year from the learning path, retaining the disagreement in notes.
  for u in L['units']+[L['test']]:
   for s in u['steps']:
    if s['id']=='bp3.u3.02':s['text'][0]=B('Maniram addressed a petition to Moffatt Mills, whose inquiry examined Assam’s administration in the 1850s.','১৮৫০ৰ দশকত অসমৰ প্ৰশাসন পৰীক্ষা কৰা মফাট মিলছলৈ মণিৰামে আবেদন দিছিল।')
    if s['id']=='bp3.u3.03':s['tokens']={'en':['Maniram','petitioned','Welsh.'],'as':['মণিৰামে','ৱেল্‌চলৈ','আবেদন','দিছিল।']};s['wrong']={'en':2,'as':1}
    if s.get('why') and '1852' in s['why'].get('en',''):s['why']=B('Born 1806 → Assam Company 1839 → petition in the 1850s → revolt 1857 → execution 1858.','জন্ম ১৮০৬ → অসম কোম্পানী ১৮৩৯ → ১৮৫০ৰ দশকৰ আবেদন → ১৮৫৭ৰ বিদ্ৰোহ → ১৮৫৮ৰ ফাঁচী।')
    if s['type']=='story':
     s['text']=[B(p['en'].replace('or chief minister','a senior official'),p['as'].replace('অৰ্থাৎ মুখ্য মন্ত্ৰী','এজন জ্যেষ্ঠ বিষয়া')) for p in s['text']]
  old=L['units'][4]['steps'][2];new=map_question(old['q'],'jorhat',['jorhat','nazira','golaghat'],old['why']);new['id']=old['id'];L['units'][4]['steps'][2]=new
  L['units'][2]['learned']=[p if '1852' not in p['en'] else B('Maniram petitioned Moffatt Mills about grievances','মণিৰামে অভিযোগৰ বিষয়ে মফাট মিলছলৈ আবেদন দিছিল') for p in L['units'][2]['learned']]
 # Use the four already-authored learned points for additional retrieval, with explicit options.
 for u in L['units']:
  ex=[s for s in u['steps'] if s['type']!='story'];needed=max(0,5-len(ex))
  # Additional exercises are authored in the supplement file, not inferred answers.
  supplements=read(ROOT/'docs/authoring/british_draft_supplements.json')[f"{n}.{u['id']}"]
  for i,s in enumerate(supplements):s['id']=f"bp{n}.{u['id']}.supp.{i+1:02}";u['steps'].append(s)
  if len([s for s in u['steps'] if s['type']!='story'])<5:raise ValueError(f'Insufficient exercises: {L["id"]}/{u["id"]}')
 L['review_notes']='Expanded bilingual draft, 2026-11-02. Previous unresolved notes: '+L.get('review_notes','')+' Petition year and exact Khamti attack day are omitted where disputed. Fluent Assamese editorial review remains pending.'
 all_lessons.append(L);C['kings'][n-1].update({'lesson':L['id'],'face':L['portrait']})
# Shared glossary: retain permanent existing identifiers and introduce new work/person names.
for brief in briefs.values():
 for u in brief['units']:
  for f in u['facts']:
   if f[4] not in ('person','work','institution','movement','term','title'):continue
   eid=re.sub(r'[^a-z0-9]+','-',f[2].lower()).strip('-')
   if not eid or eid in ENT:continue
   ENT[eid]={'type':'person' if f[4]=='person' else 'term','name':B(f[2],f[3]),'meaning':B(f[0]+' '+f[2],f[1]+' '+f[3])}
for L in all_lessons:save(L,ROOT/f"content/lessons/{L['id']}.json")
C.pop('draft',None);C['subtitle']=B('1824–1947 · 18 lessons · 75 units','১৮২৪–১৯৪৭ · ১৮টা পাঠ · ৭৫টা অধ্যায়')
save(C,ROOT/'content/courses/british-period.json');save(bank,ROOT/C['bank']);save(ENT,ROOT/'content/entities.json')
cat=read(ROOT/'content/catalog.json');S=next(s for s in cat['subjects'] if s['id']=='assam-history')
for i,row in enumerate(S['courses']):
 if row.get('soon') and row['title']['en'].lower().startswith('british'):S['courses'][i]={'course':CID};break
else:raise ValueError('Missing course slot in catalog')
save(cat,ROOT/'content/catalog.json')
save({'date':'2026-11-02','source_library':str(LIB),'rights':'User authorised reuse; source project CC BY-NC-ND content. Historical scenes are modern artistic interpretations.','assets':assets},ROOT/'docs/research/british-assets.json')
save({'date':'2026-11-02','sources':sources,'notes':['Historical and Assamese editorial review status is recorded in each lesson.','No fabricated PYQ labels or human-review claims.','Catalogue/index sources are distinguished from actual primary passages.']},ROOT/'docs/research/british-source-register.json')
print('Integrated',len(all_lessons),'lessons,',sum(len(L['units']) for L in all_lessons),'units,',len(bank['questions']),'bank questions')
