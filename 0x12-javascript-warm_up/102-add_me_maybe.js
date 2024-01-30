#!/usr/bin/node
// function that increments & calls a function
exports.addMeMaybe = function addMeMaybe (number, theFunction) {
    return theFunction(++number);
}