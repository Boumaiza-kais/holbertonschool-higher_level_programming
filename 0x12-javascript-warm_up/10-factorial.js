#!/usr/bin/node

const n = parseInt(process.argv[2]);

function fac (n) {
  if (n === 0 || n === 1)
    return 1;
  else if (isNaN(n)) return 1;
  else return fac(n - 1) * n;
}

console.log(fac(n));
