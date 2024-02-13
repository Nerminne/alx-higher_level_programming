#!/usr/bin/node

const num = Number(process.argv[2]);
if (typeof (num) !== 'number') {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < num; i++) {
    console.log('C is fun');
  }
}
