#!/usr/bin/node
const myArg = process.argv.slice(2);
if (isNaN(myArg[0])) {
  console.log('Not a number');
} else {
  console.log(`My number: ${myArg[0]}`);
}
