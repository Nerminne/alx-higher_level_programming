#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
const charact = 'https://swapi-api.alx-tools.com/api/people/18/';
let filmNum = 0;
request.get(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    const films = JSON.parse(body).results;
    for (let i = 0; i < films.length; i++) {
      for (let x = 0; x < films[i].characters.length; x++) {
        if (films[i].characters[x] === charact) {
          filmNum++;
          break;
        }
      }
    }
    console.log(filmNum);
  } else {
    console.log(`Error Code: ${response.statusCode}`);
  }
});
