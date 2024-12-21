#!/usr/bin/node
const Squared = require('./5-square');
class Square extends Squared {
  size;
  constructor (size) {
    super(size, size);
    this.size = size;
  }

  charPrint (c) {
    const char = c || 'X';
    for (let i = 0; i < this.size; ++i) {
      console.log(char.repeat(this.size));
    }
  }
}

module.exports = Square;
