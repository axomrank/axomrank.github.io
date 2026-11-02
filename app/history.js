/* Searchable reference across the integrated history curriculum. */
(async () => {
'use strict';
const {B,T,N}=AXOM;
const escape=s=>String(s??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const bt=o=>T(B(escape(o.en),escape(o.as)));
document.body.innerHTML=`<input type="checkbox" id="as" aria-label="Show in Assamese"><div class="stage"><main class="device home-page"><div class="view on"><div class="p-top"><a class="back-hub" href="index.html?subject=assam-history">‹ ${T(B('Assam History','অসমৰ ইতিহাস'))}</a><span class="spacer"></span><label class="lang" for="as"><span class="en">অ</span><span class="as">EN</span></label></div><div class="p-scroll"><section class="c-hero"><div class="eyebrow">${T(B('Explore Assam History','অসমৰ ইতিহাস অনুসন্ধান কৰা'))}</div><h1>${T(B('Timeline & index','সময়ৰেখা আৰু সূচী'))}</h1><p>${T(B('Follow events,find people and places,and return to the source lesson.','ঘটনা অনুসৰণ কৰা,মানুহ আৰু ঠাই বিচাৰা,উৎসৰ পাঠলৈ উভতা।'))}</p></section><div class="reference-controls"><div role="tablist" class="tabs"><button role="tab" id="events" aria-selected="true">${T(B('Timeline','সময়ৰেখা'))}</button><button role="tab" id="names" aria-selected="false">${T(B('People & places','মানুহ আৰু ঠাই'))}</button></div><label for="search">${T(B('Search','বিচাৰা'))}</label><input id="search" type="search" autocomplete="off"><label for="course-filter">${T(B('Course','পাঠ্যক্ৰম'))}</label><select id="course-filter"></select><label class="reference-check"><input id="deep" type="checkbox">${T(B('Include the optional Ahom deep dive','ঐচ্ছিক আহোমৰ বিশদ পাঠ সামৰা'))}</label></div><p id="result-count" class="tab-intro" aria-live="polite"></p><div id="reference-results"></div><p class="p-foot">${T(B('Dates and uncertainties follow the linked lessons. Open a lesson for its sources.','চন আৰু অনিশ্চয়তা সংযুক্ত পাঠৰ অনুসৰি।উৎসৰ বাবে পাঠ মুকলি কৰা।'))}</p></div></div></main></div>`;
AXOM.initLang();
try {
const data=await AXOM.getJSON('content/history-reference.json');
const filter=document.querySelector('#course-filter');filter.innerHTML=`<option value="">All courses · সকলো পাঠ্যক্ৰম</option>`+data.courses.map(c=>`<option value="${escape(c.id)}">${escape(c.title.en)} · ${escape(c.title.as)}</option>`).join('');
if(data.courses.filter(c=>!c.optional).length===1){filter.hidden=true;document.querySelector('label[for=course-filter]').hidden=true;}
let tab='events';
const href=id=>'lesson.html?id='+encodeURIComponent(id);
function render(){
 const q=document.querySelector('#search').value.trim().toLocaleLowerCase(),cid=filter.value,deep=document.querySelector('#deep').checked;
 const eligible=id=>data.lessons[id]&&(!cid||data.lessons[id].course===cid)&&(deep||data.lessons[id].course!=='ahom-kings');
 const match=o=>!q||JSON.stringify(o).toLocaleLowerCase().includes(q);
 let rows;
 if(tab==='events')rows=data.events.filter(e=>eligible(e.lesson)&&match([e.date,e.title,data.lessons[e.lesson].title])).map(e=>`<article class="reference-entry"><b class="reference-year">${N(e.date)}</b><div><h3>${bt(e.title)}</h3><a href="${href(e.lesson)}">${bt(data.lessons[e.lesson].title)} ›</a></div></article>`);
 else rows=data.entities.filter(e=>e.lessons.some(eligible)&&match([e.name,e.meaning,e.type])).sort((a,b)=>a.name.en.localeCompare(b.name.en)).map(e=>`<article class="reference-entry reference-name"><div><h3>${bt(e.name)}</h3><p>${bt(e.meaning)}</p><div class="reference-links">${e.lessons.filter(eligible).map(id=>`<a href="${href(id)}">${bt(data.lessons[id].title)} ›</a>`).join('')}</div></div></article>`);
 document.querySelector('#reference-results').innerHTML=rows.join('')||`<p class="tab-intro">${T(B('No matches.Try another name or course.','মিল নাই।আন নাম বা পাঠ্যক্ৰম চেষ্টা কৰা।'))}</p>`;
 document.querySelector('#result-count').innerHTML=N(rows.length)+' '+T(B('entries','টা প্ৰবিষ্টি'));
}
for(const id of ['events','names'])document.querySelector('#'+id).onclick=()=>{tab=id;for(const key of ['events','names'])document.querySelector('#'+key).setAttribute('aria-selected',String(key===tab));render()};
for(const selector of ['#search','#course-filter','#deep'])document.querySelector(selector).addEventListener(selector==='#search'?'input':'change',render);
render();
} catch(error){document.querySelector('#reference-results').innerHTML=`<p class="tab-intro">${T(B('The reference could not load.Connect once and try again.','সূচী মুকলি হোৱা নাই।এবাৰ সংযোগ কৰি পুনৰ চেষ্টা কৰা।'))}</p>`;}
})();
