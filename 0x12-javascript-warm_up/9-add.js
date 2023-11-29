#!/usr/bin/node
(function add (a, b) {
  console.log(a + b);
})(parseInt(process.argv[2]), parseInt(process.argv[3]));
