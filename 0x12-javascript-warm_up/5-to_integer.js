#!/usr/bin/node
const process = require('process');
const args = process.argv;
const myVar = args[2];

// Convert myVar to an integer
const num = parseInt(myVar, 10);

// Check if num is a valid number
if (isNaN(num)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + num);
}
