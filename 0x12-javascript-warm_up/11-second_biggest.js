#!/usr/bin/node
const arr = process.argv.slice(2);
if (arr.length <= 1) {
  console.log(0);
} else {
  for (let i = 0; i < arr.length; i++) arr[i] = parseInt(arr[i]);
  let max = Math.max(...arr);
  arr[arr.indexOf(max)] = -Infinity;
  let smax = Math.max(...arr);
  console.log(smax);
}
