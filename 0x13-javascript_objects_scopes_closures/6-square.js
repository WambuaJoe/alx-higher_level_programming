#!/usr/bin/node
// create Square class

class Square extends require('./5-square') {
  // print Rectangle using 'c'
  charPrint (c) {
    if (this.width > 0 && this.height > 0) {
      const charToPrint = c !== undefined ? c : 'X';
      for (let i = 0; i < this.height; i++) {
        console.log(charToPrint.repeat(this.width));
      }
    }
  }
}

module.exports = Square;
