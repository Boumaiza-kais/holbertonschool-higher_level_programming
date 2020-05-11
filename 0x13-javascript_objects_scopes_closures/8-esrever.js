#!/usr/bin/node
exports.esrever = function (list) {
  const esr = [];
  for (let i = list.length - 1; i >= 0; i--) {
    esr.push(list[i]);
  }
  return esr;
};
