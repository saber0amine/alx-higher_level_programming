#!/usr/bin/node

const fs = require('fs');

const args = process.argv;

const [fileA, fileB, fileC] = [args[2], args[3], args[4]];

const dataA = fs.readFileSync(fileA, 'utf8');
const dataB = fs.readFileSync(fileB, 'utf8');
fs.writeFileSync(fileC, dataA + dataB);
