#!/usr/bin/node

// A script that searches the second biggest integer in the list of arguments.
// You can assume all arguments can be converted to integer
// If no argument passed, print 0
// If the number of arguments is 1, print 0
// You must use console.log(...) to print all output
// You are not allowed to use var

const args = process.argv;
if (args.length <= 3) {
  console.log(0);
} else {
  const arg = args.map(Number)
    .slice(2)
    .sort((a, b) => a - b);
  console.log(arg[arg.length - 2]);
}
