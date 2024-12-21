#!/usr/bin/node
const fs = require('fs');

// Get file paths from command-line arguments
const [sourceFile1, sourceFile2, destinationFile] = process.argv.slice(2);

// Read and concatenate the files, then write to the destination
fs.writeFileSync(destinationFile, fs.readFileSync(sourceFile1) + '\n' + fs.readFileSync(sourceFile2));
