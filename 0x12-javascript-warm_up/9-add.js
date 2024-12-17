#!/usr/bin/node
const process = require('process');
const arg = process.argv;
const var1 = parseInt(arg[2], 10);
const var2 = parseInt(arg[3], 10);
add(var1, var2);
function add (a, b) {
  const sum = a + b;
  console.log(sum);
}
