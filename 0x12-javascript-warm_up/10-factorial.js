#!/usr/bin/node

function factorial (a) {
  if (a === 0) { console.log(1); } else {
    let fact = 1;
    for (let i = a; i > 0; i--) { fact *= i; }
    console.log(fact);
  }
}

factorial(parseInt(process.argv[2]));
