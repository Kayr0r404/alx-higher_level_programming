#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if ((w === 0 || w < 0) || (h === 0 || h < 0)) {
      new Object();
    } else if (w && h) {
      this.width = w;
      this.height = h;
    }
  }
};
