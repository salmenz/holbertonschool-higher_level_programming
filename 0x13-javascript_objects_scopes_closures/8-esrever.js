#!/usr/bin/node
exports.esrever = function (list) {
  const revlist = [];
  const l = list.length;
  for (let i = 0; i < l; i++) {
    const item = list.pop();
    revlist.push(item);
  }
  return revlist;
};
