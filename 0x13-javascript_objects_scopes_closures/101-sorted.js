#!/usr/bin/node

const d = require('./101-data').dict;

const usersByOccurrence = {};
for (const userId in d) {
  const occurrences = d[userId];

  if (!usersByOccurrence[occurrences]) {
    usersByOccurrence[occurrences] = [];
  }
  usersByOccurrence[occurrences].push(userId);
}
console.log(usersByOccurrence);
