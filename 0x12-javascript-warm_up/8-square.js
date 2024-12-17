#!/usr/bin/node
const process = require('process');
const arg = process.argv;
const myVar = parseInt(arg[2], 10);
if (isNaN(myVar)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < myVar; i++) {
    let row = '';
    for (let j = 0; j < myVar; j++) {
      row += 'X';
    }
    console.log(row);
  }
}
