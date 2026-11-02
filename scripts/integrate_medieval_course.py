#!/usr/bin/env python3
"""One-time import of curated medieval briefs and expanded Koch drafts."""
import copy,csv,hashlib,json,shutil,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT/'docs/authoring'))
from medieval_new_units import LESSONS
from medieval_supplements import S
from compile_history_units import compile_unit,bank_questions
from lesson_authoring import bi as B,identify,new_test,who,map_question
LIB=Path('/home/angsuman/extra_spac/Assam History')
def read(p):return json.loads(Path(p).read_text())
def save(o,p):Path(p).parent.mkdir(parents=True,exist_ok=True);Path(p).write_text(json.dumps(o,ensure_ascii=False,indent=1)+'\n')
C=read(ROOT/'private/drafts/medieval-kingdoms/course.json');CID=C['id']
if (ROOT/f'content/courses/{CID}.json').exists():raise SystemExit('Already imported; edit published JSON without regenerating ids.')
rows={r['id']:r for r in csv.DictReader(open(LIB/'data/assam_history.csv',encoding='utf-8-sig'))};assets=[]
def asset(sid):
 r=rows[sid];src=LIB/r['scene_image'];dest=ROOT/f'content/media/{CID}/{sid.lower()}.webp';dest.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(src,dest)
 rel=f'{CID}/{dest.name}'
 if not any(a['file']==rel for a in assets):assets.append({'file':rel,'source_record':sid,'source_file':r['scene_image'],'sha256':hashlib.sha256(src.read_bytes()).hexdigest(),'kind':'modern artistic reconstruction'})
 return rel
sources={
 'gait':{'title':'Edward Gait, A History of Assam (1906), medieval and early Ahom chapters','url':'https://ignca.gov.in/Asi_data/34806.pdf','used_for':'Retrospective narrative compared with local source-library notes. Early dynastic dates are not treated as contemporary inscriptions.'},
 'raids':{'title':'Source-library western Assam storyline and Gait, medieval chapters','local_source':'Assam History/research; data/assam_history.csv, KAMATA records','used_for':'1206 and 1220s frontier expeditions; names and uncertain identifications distinguished from Kanai inscription.'},
 'kanai':{'title':'IGNCA, Rock Art in Assam report (2015)','url':'https://ignca.gov.in/rockart_2015/Rockart_AssamReport2015.pdf','used_for':'Kanai Barasi Bowa, conventional date 1206; a short inscription is not a full royal biography.'},
 'sandhya':{'title':'Gait and source-library Kamata research: Sandhya and Yuzbak','local_source':'Assam History/research; KAMATA scene records','used_for':'Conventional 1257 account and transfer to Kamata. Precise accession chronologies remain secondary reconstructions.'},
 'cooch':{'title':'Cooch Behar district, Royal History','url':'https://coochbehar.gov.in/about-district/history/','used_for':'Khen succession, Husain Shah and 1498. Koch accession dates differ between this page and other chronologies; avoid exact accession tests.'},
 'archaeology':{'title':'Assam Directorate of Archaeology, protected monuments','url':'https://archaeology.assam.gov.in/information-services/detail/list-of-protected-archaeological-sites-and-monuments)','used_for':'Archaeological context and the distinction between remains and later narratives.'},
 'bhuyans':{'title':'A Tribute to Sankaradeva, Baro-Bhuyan history','url':'https://atributetosankaradeva.org/barabhuyan.htm','used_for':'Bhuyan chiefs and Sankardev’s family; a confederate title, not an invariant count of twelve.'},
 'sankardev':{'title':'Traditional Sankardev biographies and the source-library Koch research','local_source':'Assam History/research; KOCH-09, KOCH-11, KOCH-20','used_for':'Bordowa, Koch protection and traditional account of the woven cloth; do not identify every surviving museum textile as the original sixteenth-century commission.'},
 'chutia':{'title':'Source-library Chutia research, cross-checked with Gait','local_source':'Assam History/research; CHUTIA scenes; Gait chapter V','used_for':'Sadiya and conquest in 1523–24; legendary founder chronologies omitted.'},
 'tamreswari':{'title':'Archaeological Survey of India, ruins of Copper Temple near Paya','url':'https://www.asiguwahaticircle.gov.in/coppertemple.html','used_for':'Dikkaravasini identification and reported Muktadharmanarayana inscription. Shrine traditions and Deori ritual history are distinguished from the surviving remains.'},
 'dimasa':{'title':'Assam Tourism, Maibang','url':'https://assamtourism.gov.in/maibang.php','used_for':'Maibang as a Dimasa capital during the sixteenth to eighteenth centuries.'},
 'cachar':{'title':'Census of India 2011, Cachar District Census Handbook part A','url':'https://censusindia.gov.in/nada/index.php/catalog/200/download/450/DH_2011_1817_PART_A_DCHB_CACHAR.pdf','used_for':'Khaspur, Govindachandra and annexation of plains Cachar in 1832; hill territory treated separately.'},
 'jaintia':{'title':'Census of India 2011, Jaintia Hills District Census Handbook part B','url':'https://censusindia.gov.in/nada/index.php/catalog/865/download/36328/DH_2011_1707_PART_B_DCHB_JAINTIA_HILLS.pdf','used_for':'Nartiang, Jaintiapur, annexation in 1835 and matrilineal social institutions.'},
 'manipur':{'title':'Bishnupur district, history','url':'https://bishnupur.nic.in/history/','used_for':'Bhagyachandra and Vaishnava cultural patronage; exact first Ras performance date omitted where traditions differ.'},
 'tripura':{'title':'Tripura Legislative Assembly, short history','url':'https://www.tripuraassembly.nic.in/short%20history%20of%20tla.pdf','used_for':'Manikya dynasty and the neighbouring kingdom; no literal endorsement of mythical ancient king lists.'},
 'moran-matak':{'title':'Tinsukia district, district at a glance','url':'https://tinsukia.assam.gov.in/index.php/about-district/district-glance','used_for':'Sarbananda and Bengmara; early Moran and Borahi chiefs come from the separately identified Buranji tradition.'},
 'textile':{'title':'British Museum curator Richard Blurton, Krishna in the Garden of Assam lecture, University of Bonn','url':'https://www.ioa.uni-bonn.de/aik/de/nachrichten/online-lecture-by-dr-richard-blurton-krishna-in-the-garden-of-assam','used_for':'Surviving devotional textiles reflect Sankardev’s teaching; museum provenance differs from the traditional original commission.'}}
sources['archaeology']['url']=sources['archaeology']['url'].rstrip(')')
ENT=read(ROOT/'content/entities.json')
for k,v in read(ROOT/'private/drafts/medieval-kingdoms/entities.json').items():
 if k in ENT and ENT[k]!=v:raise ValueError(k)
 ENT[k]=v
pools={}
for L in LESSONS.values():
 for u in L['units']:
  if 'borrow' in u:continue
  for f in u['facts']:
   if B(f[2],f[3]) not in pools.setdefault(f[4],[]):pools[f[4]].append(B(f[2],f[3]))
seeds={'region':[('Bengal','বংগ'),('Tibet','তিব্বত'),('Cachar','কাছাৰ'),('Kamata','কামতা')], 'term':[('Paik','পাইক'),('Khel','খেল'),('Buranji','বুৰঞ্জী'),('Narayani','নাৰায়ণী')], 'kingdom':[('Ahom','আহোম'),('Koch','কোচ'),('Tripura','ত্ৰিপুৰা'),('Jaintia','জয়ন্তীয়া')], 'dynasty':[('Varman','বৰ্মন'),('Pala','পাল'),('Khen','খেন'),('Manikya','মাণিক্য')], 'number_word':[('Twelve','বাৰ'),('Always twelve','সদায় বাৰ'),('One','এক'),('Ten','দহ')], 'year_range':[('1523–24','১৫২৩–২৪'),('1832–54','১৮৩২–৫৪'),('1603–15','১৬০৩–১৫'),('1662–63','১৬৬২–৬৩')], 'community':[('Deori','দেউৰী'),('Moran','মৰাণ'),('Borahi','বৰাহী'),('Dimasa','ডিমাছা')], 'office':[('Borphukan','বৰফুকন'),('Borbarua','বৰবৰুৱা'),('Burhagohain','বুঢ়াগোহাঁই'),('Sadiyakhowa Gohain','শদিয়াখোৱা গোহাঁই')], 'work':[('Buranji','বুৰঞ্জী'),('Rajmala','ৰাজমালা'),('Harshacharita','হৰ্ষচৰিত'),('Kirtan Ghosa','কীৰ্তন ঘোষা')], 'event':[('Treaty of Majuli','মাজুলীৰ সন্ধি'),('Battle of Saraighat','শৰাইঘাটৰ যুদ্ধ'),('Treaty of Yandabo','ইয়াণ্ডাবু সন্ধি'),('Turbak’s defeat','তুৰ্বকৰ পৰাজয়')]}
seeds['group']=[('Bhuyans','ভূঞাসকল'),('Paiks','পাইকসকল'),('Priests','পুৰোহিতসকল'),('Monks','সন্ন্যাসীসকল')]
seeds['social']=[('Matrilineal','মাতৃবংশীয়'),('Patrilineal','পিতৃবংশীয়'),('Bilateral','উভয়বংশীয়'),('Royal succession','ৰাজউত্তৰাধিকাৰ')]
for k,vals in seeds.items():
 for pair in vals:
  if B(*pair) not in pools.setdefault(k,[]):pools[k].append(B(*pair))
all_lessons=[];bank={'note':'Original source-linked practice. No past-paper attribution.','questions':[]}
for n,brief in sorted(LESSONS.items()):
 lid=C['kings'][n-1]['id'];us=[];extra_sources=[];show=['brahmaputra','guwahati','sadiya','dimapur','cooch-behar']
 for u in brief['units']:
  if 'borrow' in u:
   src=read(ROOT/f"content/lessons/{u['borrow']['lesson']}.json");old=next(x for x in src['units'] if x['id']==u['borrow']['unit']);nu=copy.deepcopy(old);nu['id']=u['id'];nu['title']=B(*u['title']);nu['steps']=[s for s in nu['steps'] if s['type']!='mcq'];nu['steps'].sort(key=lambda s:s['type']!='story')
   for s in nu['steps']:
    s.pop('id',None)
    if s.get('img') and '/' not in s['img']:s['img']=src['id']+'/'+s['img']
    if s['type']=='picture':s['options']=[x if '/' in x else src['id']+'/'+x for x in s['options']]
    if s['type']=='map':s['map']=src['map']
   extra_sources+=src['sources'];us.append(nu)
  else:
   for c in u['cards']:
    if c.get('scene'):c['img']=asset(c.pop('scene'))
   us.append(compile_unit(u,pools,lid+'.'+u['id']))
 portrait=next((s['img'] for u in us for s in u['steps'] if s.get('img')),asset('KOCH-25'))
 L={'id':lid,'course':CID,'no':n,'version':1,'eyebrow':B('Assam History · Medieval kingdoms','অসমৰ ইতিহাস · মধ্যযুগৰ ৰাজ্য'),'king':B(*brief['title']),'reign':B(*brief['span']),'portrait':portrait,'map':{'box':[88.5,23,96.8,28.7],'show':show},'guide':{'timeline':[]},'sources':[sources[k] for k in brief['source_keys']]+extra_sources,'units':us,'test':new_test([s for u in us for s in [x for x in u['steps'] if x['type']!='story'][:2]]),'review_notes':'AI-assisted bilingual draft. Historical uncertainty is explicit; fluent Assamese editorial review pending. Borrowed units adapted with new ids from the existing Ahom deep dive.'}
 identify(L,lid);all_lessons.append(L)
 era=next(e['id'] for e in C['eras'] if e['from']<=n<=e['to']);bank['questions']+=bank_questions(L,[u for u in brief['units'] if 'borrow' not in u],pools,era)
# Expand foundation drafts with explicit exercises and appropriate images.
image_scenes={4:[['KOCH-01','KOCH-01'],['KOCH-02','KOCH-04'],['KOCH-03',None],['KOCH-05','KOCH-07']],5:[['KOCH-07','KOCH-10'],['KOCH-08',None],['KOCH-15','KOCH-16'],['KOCH-17',None],['KOCH-11','KOCH-09','KOCH-24'],['KOCH-22','KOCH-25']],6:[['KOCH-25',None],[None,None],[None,None]]}
for p in sorted((ROOT/'private/drafts/medieval-kingdoms/lessons').glob('*.json')):
 L=read(p);n=L['no']
 if n==4:
  u=L['units'][2];u['steps']=[s for s in u['steps'] if s['type']!='story' or s['id']!='ko4.u3.03']
  u['steps'].insert(1,{'type':'story','id':'ko4.u3.03','title':B('A story needs evidence','কাহিনীৰ প্ৰমাণ লাগে'),'text':[B('The rediscovery belongs to temple tradition. Accounts disagree about the destruction. Do not turn either Husain Shah or Kalapahar into a certain culprit without dated evidence.','পুনৰ আৱিষ্কাৰ মন্দিৰৰ পৰম্পৰাৰ কথা। ধ্বংসৰ বিৱৰণত মতভেদ আছে। তাৰিখযুক্ত প্ৰমাণ অবিহনে হুছেইন শ্বাহ বা কালাপাহাৰক নিশ্চিত দোষী নকৰিবা।')],'art':'scroll'})
  u['learned']=[B('The shrine is Kamakhya','পীঠটো কামাখ্যা'),B('Its hill is Nilachal','ইয়াৰ পাহাৰ নীলাচল'),B('The city is Guwahati','চহৰখন গুৱাহাটী'),B('Rediscovery and destruction stories require independent evidence','পুনৰ আৱিষ্কাৰ আৰু ধ্বংসৰ কাহিনীৰ স্বতন্ত্ৰ প্ৰমাণ লাগে')]
  for s in u['steps']:
   if s['type']=='tf':s['s']=B('The rediscovery story alone proves who destroyed the earlier temple.','কেৱল পুনৰ আৱিষ্কাৰৰ কাহিনীয়ে আগৰ মন্দিৰ কোনে ধ্বংস কৰিলে প্ৰমাণ কৰে।');s['answer']=False;s['why']=B('Tradition is evidence of memory; identifying a destroyer requires separate records.','পৰম্পৰা স্মৃতিৰ প্ৰমাণ; ধ্বংসকাৰীৰ চিনাক্তকৰণৰ বাবে পৃথক নথি লাগে।')
 if n==5:
  raw=json.dumps(L,ensure_ascii=False).replace('around <mark>1540</mark>','in the <mark>mid-sixteenth century</mark>').replace('প্ৰায় <mark>১৫৪০</mark> চনত','<mark>ষোড়শ শতিকাৰ মাজভাগত</mark>').replace('Malladev became King Nara Narayan, about 1540','Malladev became King Nara Narayan in the mid-sixteenth century').replace('প্ৰায় ১৫৪০ চনত মল্লদেৱ ৰজা নৰনাৰায়ণ হ\u0027ল','ষোড়শ শতিকাৰ মাজভাগত মল্লদেৱ ৰজা নৰনাৰায়ণ হয়');L=json.loads(raw)
  L['units'][0]['learned'][0]=B('Malladev became King Nara Narayan in the mid-sixteenth century','ষোড়শ শতিকাৰ মাজভাগত মল্লদেৱ ৰজা নৰনাৰায়ণ হয়')
  s=L['units'][0]['steps'][1];s.update(who([B('My early name was Sukladhwaj.','মোৰ আদি নাম শুক্লধ্বজ।'),B('My familiar name compares my army’s speed to a bird.','মোৰ পৰিচিত নামে সৈন্যৰ গতি চৰাইৰ সৈতে তুলনা কৰে।')],[B('Chilarai','চিলাৰায়'),B('Raghudev','ৰঘুদেৱ'),B('Biswa Singha','বিশ্ব সিংহ')],0,B('Chilarai recalls the kite, or chila.','চিলাৰায়ে চিলা চৰাইৰ কথা মনত পেলায়।')));s.pop('q',None)
  s=L['units'][4]['steps'][3];oldid=s['id'];s=map_question(B('Tap Barpeta, linked with the traditional weaving account.','বস্ত্ৰ বোৱাৰ পৰম্পৰাগত বিৱৰণৰ বৰপেটা টিপা।'),'barpeta',['barpeta','guwahati','garhgaon'],B('The traditional account connects the weaving with Barpeta.','পৰম্পৰাগত বিৱৰণে বোৱাক বৰপেটাৰ সৈতে জড়িত কৰে।'));s['id']=oldid;L['units'][4]['steps'][3]=s
  L['units'][4]['steps'][2]['text'][1]=B('Tradition links the commission to the Koch court. Surviving museum textiles belong to this devotional weaving tradition; their date and provenance need separate study.','পৰম্পৰাই বস্ত্ৰৰ ফৰমাচ কোচ ৰাজসভাৰ সৈতে জড়িত কৰে। সংগ্ৰহালয়ৰ বৰ্তি থকা বস্ত্ৰ এই ভক্তিমূলক বয়ন পৰম্পৰাৰ; ইয়াৰ চন আৰু ইতিহাস পৃথককৈ পঢ়িব লাগে।')
 for ui,u in enumerate(L['units']):
  stories=[s for s in u['steps'] if s['type']=='story']
  for si,s in enumerate(stories):
   sid=image_scenes[n][ui][si]
   if sid:s['img']=asset(sid);s.pop('art',None)
  for i,s in enumerate(S[f"{n}.{u['id']}"]):
   if s['type']=='picture':s['options']=[x['img'] for x in s['options']];s['answerText']=B('Kamakhya construction','কামাখ্যা নিৰ্মাণ')
   s['id']=f"{L['id']}.{u['id']}.supp.{i+1:02}";u['steps'].append(s)
  u['steps'].sort(key=lambda s:s['type']!='story')
 L['portrait']=next(s['img'] for u in L['units'] for s in u['steps'] if s.get('img'))
 # Rebuild an unpublished test after correction; unit ids remain intact.
 L['test']=new_test([s for u in L['units'] for s in [x for x in u['steps'] if x['type']!='story'][:2]])
 for i,s in enumerate(L['test']['steps'],1):s['id']=f"{L['id']}.test.{i:02}"
 L['sources']+=[sources['cooch'],sources['textile']];L['review_notes']='Expanded AI-assisted draft. Koch accession dates vary by source; uncertain temple destruction is not presented as fact. Fluent Assamese review pending.';all_lessons.append(L)
# Practice questions use only fully keyed retrieval from the released units.
for L in all_lessons:
 era=next(e['id'] for e in C['eras'] if e['from']<=L['no']<=e['to'])
 if L['no'] in LESSONS:continue
 for u in L['units']:
  for i,s in enumerate(u['steps']):
   if s['type'] not in ('whoami','inline','tf'):continue
   q={'id':f"bank.{L['id']}.{u['id']}.{i:02}",'era':era,'lesson':L['id'],'difficulty':'easy','exams':['ADRE','APSC','TET','SI'],'why':s['why']}
   if s['type']=='tf':q.update(type='tf',s=s['s'],answer=s['answer'])
   elif s['type']=='whoami':q.update(type='mcq',q=B(' · '.join(x['en'] for x in s['clues']),' · '.join(x['as'] for x in s['clues'])),options=s['options'],answer=s['answer'])
   else:q.update(type='mcq',q=B(s['before']['en']+' …',s['before']['as']+' …'),options=s['options'],answer=s['answer'])
   bank['questions'].append(q)
for L in all_lessons:
 save(L,ROOT/f"content/lessons/{L['id']}.json");C['kings'][L['no']-1].update(lesson=L['id'],face=L['portrait'],name=L['king'],reign=L['reign']['en'])
C.pop('draft',None);C['subtitle']=B('9 lessons · 35 units','৯টা পাঠ · ৩৫টা অধ্যায়');save(C,ROOT/f'content/courses/{CID}.json');save(bank,ROOT/C['bank']);save(ENT,ROOT/'content/entities.json')
cat=read(ROOT/'content/catalog.json');sub=next(s for s in cat['subjects'] if s['id']=='assam-history')
for i,r in enumerate(sub['courses']):
 if r.get('soon') and any(w in r['title']['en'].lower() for w in ['kamata','medieval']):sub['courses'][i]={'course':CID};break
else:raise ValueError('Missing catalog slot')
save(cat,ROOT/'content/catalog.json');save({'date':'2026-11-02','sources':sources},ROOT/'docs/research/medieval-source-register.json');save({'source_library':str(LIB),'rights':'User authorised reuse; modern artistic reconstructions, not evidence.','assets':assets},ROOT/'docs/research/medieval-assets.json')
print('Integrated',len(all_lessons),'lessons;',sum(len(L['units']) for L in all_lessons),'units;',len(bank['questions']),'bank questions')
