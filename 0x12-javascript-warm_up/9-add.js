#!/usr/bin/node
let process = require('process');
let arg = process.argv;
let var1 = parseInt(arg[2], 10);
let var2 = parseInt(arg[3], 10);
add(var1, var2);
function add(a, b) {
    let sum = a + b;
    console.log(sum);
}