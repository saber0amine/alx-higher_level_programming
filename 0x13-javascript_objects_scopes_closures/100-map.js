#!/usr/bin/node

const l = require('./100-data').list;

console.log(l);
const nl = l.map((value, index) => value * index);
console.log(nl);
