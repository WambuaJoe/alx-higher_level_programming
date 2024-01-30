#!/usr/bin/node
// execute function x number of times
exports.callMeMoby = function (x, theFunction) {
  for (let a = 0; a < x; a++) theFunction();
};
