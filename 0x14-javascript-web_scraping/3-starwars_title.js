#!/usr/bin/node

const request = require('request');
request.get('https://swapi.co/api/films/' + process.argv[2], function (err, response, body) {
  if (err) console.log(error);
  else console.log(JSON.parse(body).title);
});
