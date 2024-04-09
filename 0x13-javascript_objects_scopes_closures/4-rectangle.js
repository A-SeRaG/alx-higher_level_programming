#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if ((w > 0) && (h > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let s;
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        s += 'X';
      }
      console.log(s);
    }
  }

  rotate () {
    let a = this.height;
    this.height = this.width;
    this.width = a;
  }

  double () {
    this.height = 2 * this.height;
    this.width = 2 * this.width;
  }
}

module.exports = Rectangle;
