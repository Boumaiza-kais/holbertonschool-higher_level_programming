#!/usr/bin/node

const Square10 = require('./5-square');

module.exports = class Square extends Square10 {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) this.print()
     else {
      for (let i = 0; i < this.width; i++) {
        console.log(c.repeat(this.height));
      }
    }
  }
};
