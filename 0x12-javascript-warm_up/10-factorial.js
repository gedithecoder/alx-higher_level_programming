#!/usr/bin/node
const myArg = process.argv.slice(2);
if (isNaN(myArg[0])) {
  console.log('1');
}
function factorial (num) {
  if (num === (0 || 1)) {
    return 1;
  }
  return num * factorial(num - 1);
}
console.log(factorial(myArg[0]));
