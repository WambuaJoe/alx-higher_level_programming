#!/usr/bin/node
// return number of occurrences in a list
exports.nbOccurences = function (list, searchElement) {
  let counter = 0;

  for (let a = 0; a < list.length; a++) {
    counter = (list[a] === searchElement ? counter + 1 : counter);
  }
  return counter;
};
