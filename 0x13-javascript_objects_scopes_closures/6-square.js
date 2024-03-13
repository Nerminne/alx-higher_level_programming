#!/usr/bin/node
const ParentSquare = require('./5-square');

module.exports = class Square extends ParentSquare {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let col = 0; col < this.width; col += 1) {
        console.log(c.repeat(this.width));
      }
    }
  }
};
