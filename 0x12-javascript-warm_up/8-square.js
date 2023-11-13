#!/usr/bin/node

const arg = process.argv[2];
if (!isNaN(arg)) {
  for (let i = 0; i < parseInt(arg); i++) {
    let row = '';
    for (let j = 0; j < parseInt(arg); j++) { row += 'X'; }
    console.log(row);
  }
} else { console.log('Missing size'); }
