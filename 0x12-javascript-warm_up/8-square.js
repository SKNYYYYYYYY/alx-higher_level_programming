#!/usr/bin/node
let process = require('process');
let arg = process.argv
let myVar = parseInt(arg[2], 10)
if (isNaN(myVar)) {
    console.log("Missing size");
}
else {
    for (let i = 0; i < myVar; i++) {
        let row = "";
        for (let j = 0; j < myVar; j++){
            row += "X";
        }
        console.log(row);
    }
}