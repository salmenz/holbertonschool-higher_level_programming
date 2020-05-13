#!/usr/bin/node
const request = require('request');
request.get(process.argv[2], function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    let n = 0;
    const f = JSON.parse(body).results;
    for (const mov of f) {
      for (const c of mov.characters) {
        if (c.endsWith('18/')) {
          n++;
        }
      }
    }
    console.log(n);
  }
});
