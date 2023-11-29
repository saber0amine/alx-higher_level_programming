#!/usr/bin/node
const occurrences = parseInt(process.argv[2]);
// if (occurrences) {
//   for (let i = 0; i < occurrences; i++) console.log('C is fun');
// } else {
//   console.log('Missing number of occurrences');
// }
occurrences ? (function (occurrences) { for (let i = 0; i < occurrences; i++) console.log('C is fun'); })(occurrences) : console.log('missing number');
