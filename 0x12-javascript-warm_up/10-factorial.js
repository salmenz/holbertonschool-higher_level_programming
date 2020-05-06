#!/usr/bin/node
function factorial (n = 0) {
  if (n === 0 || n === 1) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}
console.log(factorial(process.argv[2]));
