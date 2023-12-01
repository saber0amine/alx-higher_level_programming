#!/usr/bin/node
if (process.argv[2] === undefined || isNaN(process.argv[2])) {
  console.log('Missing size');
} else {
  const args = Number(process.argv[2]);
  let i = 0;
  while (i < args) {
    console.log('X'.repeat(args));
    i++;
  }
}
