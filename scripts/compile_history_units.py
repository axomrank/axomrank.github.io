"""Compile curated history unit briefs into the existing lesson schema.

Briefs provide the narrative, translations, facts, misconception, sources and
interaction. This module assembles UI fields; it does not research or translate.
Only use this for new lessons: never replace a published lesson's permanent ids.
"""
import copy
import hashlib
import random
from lesson_authoring import bi, story, tf, match, inline, unit, new_test, identify


def rng(key):
    return random.Random(int(hashlib.sha256(key.encode()).hexdigest()[:16], 16))


def options(fact, pools, key):
    answer = bi(fact[2], fact[3])
    candidates = [x for x in pools[fact[4]] if x != answer]
    if len(candidates) < 3:
        raise ValueError(f"Need three plausible distractors for {fact}")
    out = [answer] + rng(key).sample(candidates, 3)
    rng(key + ':shuffle').shuffle(out)
    return out, out.index(answer)


def compile_unit(brief, pools, prefix):
    facts = brief['facts']
    if len(facts) != 4 or len({(f[2], f[3]) for f in facts}) != 4:
        raise ValueError('Provide four distinct facts for matching')
    cards = []
    for card in brief['cards']:
        s = {'type':'story','title':bi(*card['title']),
             'text':[bi(*paragraph) for paragraph in card['text']]}
        if card.get('img'): s['img'] = card['img']
        elif card.get('map'): s['map'] = card['map']
        else: s['art'] = card.get('art','scroll')
        if card.get('link'): s['link'] = card['link']
        cards.append(s)
    ops, answer = options(facts[0], pools, prefix + ':inline')
    exercises = [
        inline(bi(facts[0][0],facts[0][1]),bi('.','।'),ops,answer,
               bi(facts[0][0]+' '+facts[0][2]+'.',facts[0][1]+' '+facts[0][3]+'।')),
        tf(bi(*brief['trap']['statement']),False,bi(*brief['trap']['why'])),
        match([[bi(f[0],f[1]),bi(f[2],f[3])] for f in facts],
              bi(*brief['connections'])),
    ]
    fact = facts[1]
    ops, answer = options(fact,pools,prefix+':fill')
    exercises.append({'type':'fill','before':bi(fact[0],fact[1]),'after':bi('.','।'),
                      'answer':fact[2], 'asOptions':[o['as'] for o in ops],
                      'asAnswer':answer,'answerText':bi(fact[2],fact[3]),
                      'why':bi(fact[0]+' '+fact[2]+'.',fact[1]+' '+fact[3]+'।')})
    exercises.append(copy.deepcopy(brief['interaction']))
    if brief.get('extra'): exercises.append(copy.deepcopy(brief['extra']))
    # Narrative remains in order; exercises follow a deliberately varied order.
    rng(prefix).shuffle(exercises)
    return unit(brief['id'],bi(*brief['title']),
                [bi(f[0]+' '+f[2],f[1]+' '+f[3]) for f in facts],cards+exercises,
                brief.get('icon','star'))


def compile_lesson(meta, briefs, pools):
    lesson = copy.deepcopy(meta)
    prefix = meta['id']
    lesson['units'] = [compile_unit(b,pools,prefix+'.'+b['id']) for b in briefs]
    # Select a balanced two-question sample from every unit, with fresh test ids.
    selected = []
    for index,u in enumerate(lesson['units']):
        ex=[s for s in u['steps'] if s['type']!='story']
        selected.extend([ex[index % len(ex)],ex[(index+2) % len(ex)]])
    lesson['test'] = new_test(selected)
    return identify(lesson,prefix)


def bank_questions(lesson, briefs, pools, era):
    questions=[]
    for brief in briefs:
        facts=brief['facts']
        for index,fact in enumerate(facts):
            key=f"bank.{lesson['id']}.{brief['id']}.{index+1:02}"
            ops,answer=options(fact,pools,key)
            questions.append({'id':key,'type':'mcq','era':era,'lesson':lesson['id'],
                'difficulty':'easy','exams':['ADRE','TET','APSC','SI'],
                'q':bi(lesson['king']['en']+' · '+brief['title'][0]+'<br>'+fact[0]+' …',
                       lesson['king']['as']+' · '+brief['title'][1]+'<br>'+fact[1]+' …'),
                'options':ops,'answer':answer,
                'why':bi(fact[0]+' '+fact[2]+'.',fact[1]+' '+fact[3]+'।')})
        # No invented past-paper attribution; these are original practice items.
    return questions
