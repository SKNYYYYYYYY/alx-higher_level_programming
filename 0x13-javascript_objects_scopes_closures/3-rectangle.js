#!/usr/bin/node
class Rectangle {
  width;
  height;
  constructor (w, h) {
    if (w <= 0 || h <= 0 || typeof w !== 'number' || typeof h !== 'number') {
      return {};
    } else {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    const char = 'X';
    for (let i = 0; i < this.height; i++) {
      console.log(char.repeat(this.width));
    }
  }
}
module.exports = Rectangle;
