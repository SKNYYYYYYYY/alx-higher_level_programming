#!/usr/bin/node
let process = require('process');
let arg = process.argv
let myVar = parseInt(arg[2], 10)

if (isNaN(myVar)) {
    console.log("1");
}
else {
    console.log(factorial(myVar));
}
    function factorial(a) {
        if (a === 0 || a === 1) {
            return 1;
        }
        return a * factorial(a - 1);

}

