#!/usr/bin/node
const process = require('process');
let args = process.argv;
let mystring = args[3] + ' is ' + args[4];
console.log(mystring);
