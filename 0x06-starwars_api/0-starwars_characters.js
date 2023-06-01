#!/usr/bin/node
// script that prints all characters in order for a given Star Wars movie

const request = require('request');
const API_URL = 'https://swapi-api.alx-tools.com/api';

function getCharacterName (url) {
  return new Promise((resolve, reject) => {
    request(url, (err, _, body) => {
      if (err) {
        reject(err);
      } else {
        const character = JSON.parse(body);
        resolve(character.name);
      }
    });
  });
}

if (process.argv.length > 2) {
  const filmId = process.argv[2];
  const filmUrl = `${API_URL}/films/${filmId}/`;

  request(filmUrl, (err, _, body) => {
    if (err) {
      console.log(err);
    } else {
      const charactersURL = JSON.parse(body).characters;
      const characterPromises = charactersURL.map(getCharacterName);

      Promise.all(characterPromises)
        .then(names => {
          console.log(names.join('\n'));
        })
        .catch(err => {
          console.log(err);
        });
    }
  });
}
