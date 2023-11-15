#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    this.width = w;
    this.height = h;
  }

  print () {
    for (let row = 0; row < this.height; row++) {
      let line = '';
      for (let col = 0; col < this.width; col++) {
        line += 'X';
      }
      console.log(line);
    }
  }
}
