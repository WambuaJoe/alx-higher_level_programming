#!/usr/bin/node

const myArgs = process.argv.slice(2);
const res = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/:id';

res(url, (err, res, body) => {
  if (err) throw err;
  console.log(JSON.parse(body).results[myArgs[0] - 1].title);
});
