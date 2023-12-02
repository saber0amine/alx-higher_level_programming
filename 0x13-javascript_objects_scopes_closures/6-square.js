#!/usr/bin/node

module.exports = class Square extends require('./5-square') {
  charPrint (c) {
    if (!c) {
      super.print();
    } else {
      for (let i = 0; i < this.height; i++) {
        let result = '';
        for (let j = 0; j < this.width; j++) {
          result += c;
        }
        console.log(result);
      }
    }
  }
};
