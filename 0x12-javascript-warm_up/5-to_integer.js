#!/usr/bin/node
const process = require('process');
let args = process.argv;
let myVar = args[2];

// Convert myVar to an integer
let num = parseInt(myVar, 10);

// Check if num is a valid number
if (isNaN(num)) {
  console.log("Not a number");
} else {
  console.log("My number: " + num);
}
