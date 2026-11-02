#!/usr/bin/env python3
"""Split an overlong bilingual paragraph at aligned sentence boundaries.
No prose is changed. Refuse uncertain sentence alignments for editorial handling.
"""
import json,re,sys
from pathlib import Path
for path in sys.argv[1:]:
 p=Path(path);l=json.loads(p.read_text());changed=False
 for u in l['units']:
  for s in u['steps']:
   if s['type']!='story':continue
   out=[]
   for b in s['text']:
    if len(b['en'].split())<=35:out.append(b);continue
    ens=re.split(r'(?<=[.!?])\s+',b['en']);ass=[x.strip() for x in re.split(r'(?<=।)',b['as']) if x.strip()]
    if len(ens)!=len(ass) or len(ens)<2:print('MANUAL',l['id'],s['id'],len(ens),len(ass));out.append(b);continue
    chunks=[];en='';aa=''
    for e,a in zip(ens,ass):
     if en and len((en+' '+e).split())>35:chunks.append({'en':en,'as':aa});en='';aa=''
     en=(en+' '+e).strip();aa=(aa+' '+a).strip()
    chunks.append({'en':en,'as':aa})
    if any(len(c['en'].split())>35 for c in chunks):print('MANUAL-long-sentence',s['id']);out.append(b);continue
    out+=chunks;changed=True
   if len(out)>3:raise ValueError('Too many beats:'+s['id'])
   s['text']=out
 if changed:p.write_text(json.dumps(l,ensure_ascii=False,indent=1)+'\n')
