#!/usr/bin/node

const request = require('request');

const mvId = process.argv[2];

const url = 'https://swapi-api.alx-tools.com/api/films/' + mvId;

request(url, function (error, response, body) {
  if (!error && response.statusCode === 200);
  const info = JSON.parse(body);
  console.log(info.title);
});
