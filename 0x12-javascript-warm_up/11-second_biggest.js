#!/usr/bin/node
const process = require('process');
const args = process.argv;

if (args.length === 1 || args.length === 2) {
  console.log('0');
} else {
  const myArray = [];

  for (let i = 2; i < args.length; i++) {
    myArray.push(parseInt(args[i]));
  }
  const sortedArray = [...new Set (myArray.sort((a, b) => b - a))];
  console.log(sortedArray[sortedArray.length - 2]);
}
