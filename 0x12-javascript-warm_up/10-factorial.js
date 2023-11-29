#!/usr/bin/node
function factorial (n) {
  if (n) {
    return n * factorial(n - 1);
  } else {
    return 1;
  }
}
console.log(factorial(parseInt(process.argv[2])));
