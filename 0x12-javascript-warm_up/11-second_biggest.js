#!/usr/bin/node

if (process.argv.length <= 3) { console.log(1); } else {
  const numbers = process.argv.slice(2);
  const max = Math.max(...numbers);
  let secondMax = -Infinity;

  for (let i = 0; i < process.argv.length; i++) {
    if (parseInt(process.argv[i]) === max) { continue; } else {
      if (parseInt(process.argv[i]) > secondMax) {
        secondMax = parseInt(process.argv[i]);
      }
    }
  }

  console.log(secondMax);
}
