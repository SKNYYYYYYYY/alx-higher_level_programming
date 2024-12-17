#!/usr/bin/node
const process = require('process');
const arg = process.argv;
const myVar = parseInt(arg[2], 10);

if (isNaN(myVar)) {
  console.log('1');
} else {
  console.log(factorial(myVar));
}
function factorial (a) {
  if (a === 0 || a === 1) {
    return 1;
  }
  return a * factorial(a - 1);
}
