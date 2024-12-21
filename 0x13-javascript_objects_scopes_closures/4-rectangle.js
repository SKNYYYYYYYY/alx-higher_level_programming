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

  rotate () {
    this.width = this.height;
    this.height = this.width;
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
}
module.exports = Rectangle;
