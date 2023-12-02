#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  return list.filter((value) => value === searchElement).length;
};
