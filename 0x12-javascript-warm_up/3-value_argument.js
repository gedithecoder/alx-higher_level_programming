#!/usr/bin/node

const myVar = process.argv;
if (myVar.length <= 2) {
  console.log('No argument');
} else {
  console.log(myVar[2]);
}
