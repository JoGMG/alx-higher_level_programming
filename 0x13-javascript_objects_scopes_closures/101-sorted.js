#!/usr/bin/node

// A script that imports a dictionary of occurrences by user id and computes a dictionary of user ids by occurrence.
// Your script must import dict from the file 101-data.js
// In the new dictionary:
// A key is a number of occurrences
// A value is the list of user ids
// Print the new dictionary at the end

const dict = require('./101-data.js').dict;
const newDict = {};
for (const [key, val] of Object.entries(dict)) {
  if (val in newDict) {
    newDict[val].push(key);
  } else {
    newDict[val] = [key];
  }
}
console.log(newDict);
/**
 * values also == dict[key]
for (const key in dict) {
  if (dict[key] in newDict) {
    newDict[dict[key]].push(key);
  } else {
    newDict[dict[key]] = [key];
  }
}
console.log(newDict);
**/
