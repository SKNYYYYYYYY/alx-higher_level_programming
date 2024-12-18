#!/usr/bin/node
const args = process.argv.slice(2); // Extract arguments passed to the script
const firstArg = args[0] || 'No argument'; // Check if the first argument exists, default to "No argument"
console.log(firstArg);
