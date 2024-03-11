#!/usr/bin/node

function factorial (num) {
    let fact = 1;
    for (let i = num; i > 0; i--) {
    fact *= i;
  }
  return (fact);
}
let fact = factorial(process.argv[2] || 1);
console.log(fact);
