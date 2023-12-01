#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && !Number.isNaN(w) && h > 0 && !Number.isNaN(h)) {
      this.width = w;
      this.height = h;
    }
  }
};
