"""Compact notation for explicitly authored bilingual story and recall units."""
from british_new_units import C,U,W,O,T
from lesson_authoring import bi as B,tf,inline
from medieval_new_units import borrow

def D(title,stories,facts,trap,reason,interaction,scene=None):
 return U(title,[C(*title,*stories[0],scene),C('Follow the evidence','প্ৰমাণ অনুসৰণ কৰা',*stories[1])],facts,trap,reason,interaction,reason)
def X(q,ass,answers,correct,why,aw):return O(q,ass,answers,correct,why,aw)
def Who(clues,answers,correct,why,aw):return W(clues,answers,correct,why,aw)
def attach(lesson,uid,title,*ex):
 b=borrow(lesson,uid,title);b['extra']=list(ex);return b
