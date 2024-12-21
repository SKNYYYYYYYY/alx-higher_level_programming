#!/usr/bin/node
const dict = require('./101-data').dict;
const myDict = {};
for (const key in dict) {
  const value = dict[key];
  if (myDict[value]) {
    myDict[value].push(key);
  } else {
    myDict[value] = [key];
  }
}
console.log(myDict);
