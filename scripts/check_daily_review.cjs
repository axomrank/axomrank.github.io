/* Check that a short review round keeps the backlog and mixes lessons. */
const fs = require('fs');
const vm = require('vm');
const assert = require('assert/strict');

const source = fs.readFileSync('app/common.js', 'utf8');
const start = source.indexOf('const INTERVALS =');
const end = source.indexOf('function record(', start);
assert(start >= 0 && end > start, 'review functions found');

const G = { srs: {}, mistakes: {} };
for (const [lesson, count] of [['a', 5], ['b', 4], ['c', 4], ['d', 3]]) {
  for (let n = 1; n <= count; n++) G.srs[`${lesson}.${n}`] = { l: lesson, s: 0, d: '2026-11-01' };
}
G.srs['a.future'] = { l: 'a', s: 0, d: '2026-11-03' };
G.mistakes = { c: ['c.3'], d: ['d.2'], e: ['e.1'] };
const context = vm.createContext({ G, iso: () => '2026-11-02' });
vm.runInContext(source.slice(start, end), context);

const key = ({ l, id }) => `${l}:${id}`;
const total = vm.runInContext('reviewQueue()', context);
const first = vm.runInContext('dailyReviewQueue()', context);
assert.equal(total.length, 17, 'all due steps and a mistake-only step remain queued');
assert.equal(first.length, 8, 'one mission has eight questions');
assert.equal(new Set(first.map(key)).size, 8, 'round has no duplicates');
assert(first.some(({ id }) => id === 'e.1'), 'mistake-only item is included');
assert(!first.some(({ id }) => id === 'a.future'), 'future review is excluded');
assert(new Set(first.map(({ l }) => l)).size >= 4, 'first pass spreads questions across lessons');
assert.equal(vm.runInContext('reviewQueue().length', context), 17, 'selection does not consume backlog');

for (const { l, id } of first) {
  G.srs[id] = { l, s: 1, d: '2026-11-03' };
  if (G.mistakes[l]) G.mistakes[l] = G.mistakes[l].filter((item) => item !== id);
}
const second = vm.runInContext('dailyReviewQueue()', context);
assert.equal(second.length, 8, 'the next mission draws from remaining backlog');
assert(second.every((item) => !first.some((old) => key(old) === key(item))), 'answered items do not repeat immediately');
assert.equal(vm.runInContext('dailyReviewQueue(0).length', context), 0, 'zero limit is empty');
console.log('Daily review passed: bounded, varied, mistake-prioritized, backlog preserved.');
