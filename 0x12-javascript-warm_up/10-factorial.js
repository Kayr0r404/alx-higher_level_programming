#!/usr/bin/node

function factorial (a) {
  if (a === 0 && !isNaN(a)) { console.log(1); } else if (!isNaN(a)) {
    let fact = 1;
    for (let i = a; i > 0; i--) { fact *= i; }
    console.log(fact);
  } else { console.log('NaN'); }
}

factorial(parseInt(process.argv[2]));
