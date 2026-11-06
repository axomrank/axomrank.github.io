#!/usr/bin/env python3
"""Add exam-format retrieval from explicitly keyed teaching exercises.

No new fact or answer is inferred. Ordinary keyed choices, maps and matching
relations retain their source-step provenance and authored explanation. Never
label these as previous-year questions. Existing permanent bank ids are kept.
"""
import copy,hashlib,json,re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
def read(p):return json.loads(p.read_text())
def save(x,p):p.write_text(json.dumps(x,ensure_ascii=False,indent=1)+'\n')
def B(e,a):return {'en':e,'as':a}
def norm(x):return re.sub(r'\W+',' ',re.sub('<[^>]*>','',x).lower()).strip()
def sig(q):return (norm(q['q']['en']),tuple(sorted(norm(o['en']) for o in q['options'])),norm(q['options'][q['answer']]['en']))
ENT=read(ROOT/'content/entities.json');total=0;added=0
for cp in sorted((ROOT/'content/courses').glob('*.json')):
 c=read(cp);bp=ROOT/c['bank'];bank=read(bp);seen={sig(q) for q in bank['questions']};ids={q['id'] for q in bank['questions']}
 for q in bank['questions']:q['exams']=[x.lower() for x in q.get('exams',['adre','tet','apsc','si'])]
 if c['id']=='ahom-kings':save(bank,bp);total+=len(bank['questions']);continue
 for row in c['kings']:
  if not row.get('lesson'):continue
  l=read(ROOT/f"content/lessons/{row['lesson']}.json");era=next(e['id'] for e in c['eras'] if e['from']<=l['no']<=e['to'])
  for u in l['units']:
   candidates=[]
   for s in u['steps']:
    if s.get('guess'):continue
    base={'type':'mcq','era':era,'lesson':l['id'],'unit':u['id'],'difficulty':'medium','exams':['adre','tet','apsc','si'],'why':s.get('why'), 'source_step':s['id'],'practice_origin':'Adapted from an explicitly keyed lesson exercise;not a past-paper question.'}
    if s['type'] in ('mcq','odd','whoami','inline'):
     if s['type']=='whoami':question=B(' · '.join(t['en'] for t in s['clues']),' · '.join(t['as'] for t in s['clues']))
     elif s['type']=='inline':question=B(s['before']['en']+' … '+s['after']['en'],s['before']['as']+' … '+s['after']['as'])
     else:question=s['q']
     candidates.append(dict(base,q=question,options=s['options'],answer=s['answer'],suffix='choice'))
    elif s['type']=='tf':candidates.append(dict(base,q=s['s'],options=[B('True','শুদ্ধ'),B('False','অশুদ্ধ')],answer=0 if s['answer'] else 1,suffix='statement'))
    elif s['type']=='map':
     if all(x in ENT and ENT[x].get('name') for x in s['choices']):candidates.append(dict(base,q=s['q'],options=[ENT[x]['name'] for x in s['choices']],answer=s['choices'].index(s['target']),suffix='place'))
    elif s['type']=='match':
     pairs=s['pairs']
     # Repeated right-hand labels create ambiguous questions:leave those out.
     if len({norm(p[1]['en']) for p in pairs})!=len(pairs):continue
     for k,pair in enumerate(pairs):
      q=B('Match the relationship: '+pair[0]['en']+' → …','সম্পৰ্ক মিলোৱা: '+pair[0]['as']+' → …')
      candidates.append(dict(base,q=q,options=[p[1] for p in pairs],answer=k,suffix=f'pair{k+1}'))
   # Prioritise varied retrieval before multiple pairs from the same match.
   candidates.sort(key=lambda q:q['suffix'].startswith('pair'))
   picked=0
   for q in candidates:
    q['q']=B(l['king']['en']+' · '+u['title']['en']+'<br>'+q['q']['en'],l['king']['as']+' · '+u['title']['as']+'<br>'+q['q']['as'])
    if sig(q) in seen:continue
    q['id']='exam.'+q['source_step']+'.'+q.pop('suffix')
    if q['id'] in ids:continue
    q['options']=copy.deepcopy(q['options']);q['why']=copy.deepcopy(q['why'])
    bank['questions'].append(q);seen.add(sig(q));ids.add(q['id']);added+=1;picked+=1
    if picked==4:break
 bank['note']='Source-linked exam practice,including adapted keyed lesson retrieval. New questions carry source_step. No fabricated previous-year-paper attribution.'
 save(bank,bp);total+=len(bank['questions'])
print('Added',added,'practice questions;total',total)
