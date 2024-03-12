#!/usr/bin/node

let num;
if (process.argv.length <= 3) {
  num = 0;
} else {
  const arr = process.argv.slice(2).map(Number);
  for (let i = 0; i < arr.length; i++) {
    if (isNaN(arr[i])) {
      arr[i] = 0;
    }
  }
  const index = arr.indexOf(Math.max(...arr));
  arr[index] = 0;
  num = Math.max(...arr);
}
console.log(num);
