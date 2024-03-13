#!/usr/bin/node
const parentSquare = require('./5-square');

module.exports = class Square extends parentSquare {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let i = 0; i < this.width; i++) {
        console.log('C'.repeat(this.height));
      }
    }
  }
};
