/* Check the mastery model's promises with the real code from app/common.js and app/math.js. */
const fs = require('fs'), vm = require('vm'), assert = require('assert/strict');
const src = fs.readFileSync('app/common.js', 'utf8');
const piece = src.slice(src.indexOf('const BKT ='), src.indexOf('function record('));
const mergeSrc = src.slice(src.indexOf('function merge(a, b)'), src.indexOf('function applySnapshot'));
function world() {
  const c = { G: { skills: {}, miscon: {} }, day: 0, Date, Math, Object, Set, Number };
  c.iso = () => new Date(Date.UTC(2026, 0, 1) + c.day * 864e5).toISOString().slice(0, 10);
  vm.createContext(c); vm.runInContext(piece + '\n' + mergeSrc + '; this.api = { skillAnswer, skillState, rootCause, merge };', c);
  return c;
}
{ // one right answer is never mastery, typed or tapped
  const c = world(); c.api.skillAnswer('a', true, { typed: true });
  assert.equal(c.api.skillState('a'), 'learning');
  c.api.skillAnswer('a', true, { typed: true });
  assert.notEqual(c.api.skillState('a'), 'ready', 'two typed answers must not be ready');
}
{ // same-day practice alone reaches ready, never strong
  const c = world(); for (let k = 0; k < 12; k++) c.api.skillAnswer('a', true, { typed: true });
  assert.equal(c.api.skillState('a'), 'ready');
  c.day = 1; c.api.skillAnswer('a', true); assert.equal(c.api.skillState('a'), 'ready', 'one day later is not yet delayed recall');
  c.day = 4; c.api.skillAnswer('a', true); assert.equal(c.api.skillState('a'), 'strong');
}
{ // hinted successes teach nothing the model will claim
  const c = world(); for (let k = 0; k < 10; k++) c.api.skillAnswer('a', true, { hinted: true });
  assert.ok(c.G.skills.a.p <= 0.2 && c.G.skills.a.o === 0, 'a hinted success is not evidence');
}
{ // misses make a skill weak
  const c = world(); c.api.skillAnswer('a', false); c.api.skillAnswer('a', false);
  assert.equal(c.api.skillState('a'), 'weak');
}
{ // repair starts at the deepest weak prerequisite
  const c = world(), map = { a: { pre: [] }, b: { pre: ['a'] }, c: { pre: ['b'] } };
  c.api.skillAnswer('a', false); c.api.skillAnswer('b', false); c.api.skillAnswer('c', false);
  assert.equal(c.api.rootCause('c', map), 'a');
  const d = world(); assert.equal(d.api.rootCause('c', map), null, 'an untested prerequisite is not called weak');
}
{ // sync keeps the record answered last, and adds no field for a learner who never used skills
  const c = world();
  const m = c.api.merge({ skills: { a: { p: .3, t: 5 }, b: { p: .9, t: 1 } } }, { skills: { a: { p: .8, t: 9 } } });
  assert.equal(m.skills.a.p, .8); assert.equal(m.skills.b.p, .9);
  const empty = c.api.merge({ xp: 1 }, { xp: 2 });
  assert.ok(!('skills' in empty) && !('miscon' in empty), 'no new fields until used, so old account rules keep working');
}
console.log('Skill model passed: no one-answer mastery, delayed recall needed for strong, hints and sync safe.');
