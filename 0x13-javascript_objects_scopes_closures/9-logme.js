#!/usr/bin/node
// print number of args

let count = 0;
exports.logMe = function (item) {
  console.log(count + ': ' + item);
  count++;
};
