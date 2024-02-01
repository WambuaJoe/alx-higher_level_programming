#!/usr/bin/node
// create 2 instance methods
//      double() -
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

  //   exchange width & height
  rotate () {
    if (this.width > 0 && this.height > 0) {
      [this.width, this.height] = [this.height, this.width];
    }
  }

  //   multiply width & heigth by 2
  double () {
    if (this.width > 0 && this.height > 0) {
      [this.width, this.height] = [this.width * 2, this.height * 2];
    }
  }
}

module.exports = Rectangle;
