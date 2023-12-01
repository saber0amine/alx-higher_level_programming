#!/usr/bin/node
const args = process.argv[2];
if (isNaN(args) || args === undefined) {
  console.log('Missing number of occurrences');
} else {
  const argss = Number(args);
  let i = 0;

  while (i < argss) {
    console.log('C is fun');
    i++;
  }
}
