#!/usr/bin/node

console.log(isNaN(Number(process.argv[2])) ? 'Not a number' : `My number: ${Number(process.argv[2])}`);
