#!/usr/bin/node

const request = require('request');

const mv_id = process.argv[2];

let url = 'https://swapi-api.alx-tools.com/api/films/' + mv_id;

request(url, function(error, response, body) {
  if (!error && response.statusCode == 200);
    const info = JSON.parse(body);
    console.log(info.title);
});
