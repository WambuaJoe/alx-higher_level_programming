#!/usr/bin/node
const numCount = parseInt(process.argv[2]);

if (isNaN(numCount)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < numCount; i++) {
    console.log('C is fun');
  }
}
