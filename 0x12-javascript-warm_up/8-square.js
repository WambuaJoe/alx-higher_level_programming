#!/usr/bin/node
// print a square

const count = parseInt(process.argv[2]);

if (isNaN(count)) {
    console.log('Missing size');
} else {
    for (let index = 0; index < count; index++) {
        let row = '';
        for (let j = 0; j < count; j++) {
            row += 'X';            
        }
        console.log(row);
    }
}