#!/usr/bin/node
let process = require('process');
let arg = process.argv
let myVar = parseInt(arg[2], 10)
if (isNaN(myVar)) {
    console.log("Missing number of occurrences");
}
else {
    for (let i = 0; i < myVar; i++) {
        console.log("C is fun");
    }
}