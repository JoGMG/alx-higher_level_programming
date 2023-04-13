#!/usr/bin/node

// A script that prints the first argument passed to it:
// If no arguments are passed to the script, print “No argument”
// You must use console.log(...) to print all output
// You are not allowed to use var
// You are not allowed to use length

const count = process.argv[2];
console.log(count === undefined ? 'No argument' : count);
