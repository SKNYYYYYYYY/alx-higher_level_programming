#!/usr/bin/node
const process = require('process');
const args = process.argv;
const mystring = args[3] + ' is ' + args[4];
console.log(mystring);
