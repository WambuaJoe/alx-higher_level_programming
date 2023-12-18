#!/usr/bin/node
if (process.argv.slice(2)[0]) {
  const arg = process.argv[2];
  console.log(`${arg}`);
} else {
  console.log('No argument');
}
