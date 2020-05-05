#!/usr/bin/node
if (process.argv[2] && process.argv[2] !== null) {
  console.log('My number: ' + parseInt(process.argv[2]));
} else {
  console.log('Not a number');
}
