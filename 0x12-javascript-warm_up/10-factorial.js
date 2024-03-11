#!/usr/bin/node

const num = process.argv[2] || 1; let fact = 1;
for (let i = num; i > 0; i--) {
  fact *= i;
}
console.log(fact);
