#!/usr/bin/node
let process = require('process');
let args = process.argv;

if (args.length === 1 || args.length === 2) {
    console.log('0');
}
else {
    let myArray = [];

    for (let i = 2; i<args.length; i++) {
        myArray.push(parseInt(args[i]));

    }
    let sortedArray = myArray.sort();
    console.log(sortedArray[sortedArray.length - 2]);
}
