/* Run the real player state transitions with minimal view stubs. */
const fs=require('fs'),vm=require('vm'),assert=require('assert/strict');
const src=fs.readFileSync('app/engine.js','utf8');
const feedback=src.slice(src.indexOf('function feedback(right)'),src.indexOf('function next()'));
const finish=src.slice(src.indexOf('function finishUnit()'),src.indexOf('/* ---------- events ---------- */'));
function state(mode='lesson',testout=false){
 const nodes=new Map(),saved={};const node=()=>({style:{},classList:{add(){},remove(){}},focus(){}});
 const s={id:'teaching.question',type:'tf',s:{en:'A fact',as:'তথ্য'},why:{en:'Reason',as:'কাৰণ'}};
 const c={mode,VIRTUAL:mode!=='lesson',P:{done:{}},L:{id:'sample',test:{id:'test',title:{en:'Test',as:'পৰীক্ষা'},learned:[]},era:{id:'era'},eraUnits:{sample:['u1','test']}},NEXT:null,ALL:[],G:{xp:0,streak:{n:0},checkpoints:{}},
 U:{unit:null,practice:false,testout,queue:[{s,ref:s.id}],pos:0,asked:0,ok:0,xp:0,mistakes:[],done:0,total:1,st:{},start:Date.now()},B:(en,as)=>({en,as}),T:x=>typeof x==='object'?x.en:String(x),N:String,asNum:String,TR:x=>x.en,
 params:{has:()=>false},step:()=>c.U.queue[c.U.pos],lessonOf:()=>c.L.id,bankOf:()=>c.bank,
 bank:[],SFX:{good(){},bad(){},done(){}},PRAISE:[{en:'Good',as:'ভাল'}],whoXP:()=>10,surprise:()=>'',answerHTML:()=>'',saveAll(){},refresh(){},showView(){},setTimeout(){},
 $:key=>{if(!nodes.has(key))nodes.set(key,node());return nodes.get(key)},AXOM:{record(){},srsAnswer(){c.srs++},srsLearn(){c.srs++},addDayXP(){},bumpStreak(){},getLesson:id=>(saved[id]??={done:{}}),store:{set(k,v){saved[k]=v}}},srs:0};
 c.U.unit=c.L.test;c.ALL=[c.L.test];vm.createContext(c);vm.runInContext(feedback+'\n'+finish,c);return c;
}
for(const [mode,out,retry]of[['lesson',false,true],['lesson',true,false],['checkpoint',false,false],['jump',false,false]]){
 const c=state(mode,out);c.feedback(false);assert.equal(c.U.queue.length,retry?2:1,`${mode}/testout=${out} retry`);assert.equal(c.U.asked,1);
 if(retry){c.U.pos=1;c.feedback(true);assert.equal(c.U.asked,1);assert.equal(c.U.ok,0,'a successful retry cannot improve first-attempt score');}
}
for(const score of[0,7,8,10]){const c=state();c.U.asked=10;c.U.ok=score;c.finishUnit();assert.equal(!!c.P.done.test,score>=8,`normal test ${score}/10`)}
for(const score of[7,8]){const c=state('lesson',true);c.U.asked=10;c.U.ok=score;c.finishUnit();assert.equal(!!c.P.done.test,score>=8,`test-out ${score}/10`)}
for(const score of[7,8]){const c=state('checkpoint');c.U.asked=10;c.U.ok=score;c.finishUnit();assert.equal(!!c.G.checkpoints.era,score>=8,`checkpoint ${score}/10`)}
const bank=state('checkpoint');bank.U.queue[0].s._bank=true;bank.U.queue[0].s.id='exam.permanent-id';bank.feedback(false);assert.equal(bank.bank.length,0,'bank-only ids must not become unresolved lesson mistakes');assert.equal(bank.srs,0);
console.log('Learning gates passed: retries,first-attempt80%,test-outs,checkpoints and bank provenance.');
