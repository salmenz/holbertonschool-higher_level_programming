#!/usr/bin/node
const request = require('request');
const process = require('process');
const url = 'http://swapi.co/api/films/' + process.argv[2] + '/';
request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    console.log(JSON.parse(body).title);
  }
});
