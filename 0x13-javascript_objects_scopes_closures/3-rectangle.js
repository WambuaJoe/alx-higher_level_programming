#!/usr/bin/node
// create empty object after initialization
class Rectangle {
  constructor (w, h) {
    if (w >= 0 && h >= 0 && Number.isInteger(w) && Number.isInteger(h)) {
      this.width = w;
      this.height = h;
    } else {
      this.width = 0;
      this.height = 0;
    }
  }

  print () {
    if (this.width > 0 && this.height > 0) {
      for (let index = 0; index < this.height; index++) {
        console.log('X'.repeat(this.width));
      }
    }
  }
}

module.exports = Rectangle;
