#!/usr/bin/node
const myArg = process.argv.slice(2);
if (isNaN(myArg[0]) || isNaN(myArg[0])) {
  console.log('NaN');
} else {
    console.log(add(myArg[0], myArg[1]));
}
function add(a, b) {
 return +a + +b;
}
