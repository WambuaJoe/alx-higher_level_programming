#!/usr/bin/node
// print result of addition of 2 integers
function add (a, b) {
    const sum = a + b;
    console.log(sum);
}

const valInt1 = Number(process.argv[2]);
const valInt2 = Number(process.argv[3]);

if (Number.isNaN(valInt1) || Number.isNaN(valInt2)) {
    console.log('Nan');
} else {
    add(valInt1, valInt2);
}