#!/usr/bin/node
const myArg = process.argv.slice(2);
if (myArg.length === 0) {
  console.log('0');
} else if (myArg.length === 1) {
  console.log('0');
} else {
  const argv = myArg.sort(function (a, b) { return b - a; });
  console.log(argv[1]);
}
