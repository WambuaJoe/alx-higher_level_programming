#!/usr/bin/node
// create Square class

class Rectangle {
  constructor (w, h) {
    if (w >= 0 && h >= 0) {
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
      [this.width, this.height] = [this.height, this.width];
  }

  //   multiply width & heigth by 2
  double () {
      this.width *= 2;
      this.height *= 2;
}

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
}

module.exports = Square;
