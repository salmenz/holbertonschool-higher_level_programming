#!/usr/bin/node
const t = [];
if (process.argv.len < 4) {
  console.log('0');
} else {
  for (let i = 2; i < process.argv.length; i++) {
    t.push(process.argv[i]);
  }
  console.log(t.sort().reverse()[1]);
}
