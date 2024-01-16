#!/usr/bin/node
// search for 2nd biggest integer in list of args

const args = process.argv.slice(2);

if (args.length === 0 || args.length === 1) {
  console.log(0);
} else {
  let numLargest = Number.MIN_SAFE_INTEGER;
  let secondLargest = Number.MIN_SAFE_INTEGER;

  for (let a = 0; a < args.length; a++) {
    const number = parseInt(args[a]);

    if (number > numLargest) {
      secondLargest = numLargest;
      numLargest = number;
    } else if (number > secondLargest && number !== numLargest) {
      secondLargest = number;
    }
  }
  console.log(secondLargest);
}
