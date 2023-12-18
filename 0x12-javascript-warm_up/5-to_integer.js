#!/usr/bin/node

if (process.argv.slice(2)[0]) {
  const arg1 = process.argv[2];
  const valInt = parseInt(arg1, 10);
  if (!isNaN(valInt)) {
    console.log(`My number: ${valInt}`);
  } else {
    console.log('Not a number');
  }
} else {
  console.log('Not a number');
}
