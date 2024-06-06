#!/usr/bin/node

const request = require('request');
const util = require('util');

const requestPromise = util.promisify(request);

async function getCharacterName (url) {
  const response = await requestPromise(url);
  if (response.statusCode === 200) {
    console.log(JSON.parse(response.body).name);
  }
}

async function getCharactersOfMovie (movieId) {
  const url = `https://swapi.dev/api/films/${movieId}/`;
  const response = await requestPromise(url);
  if (response.statusCode === 200) {
    const characters = JSON.parse(response.body).characters;
    for (const characterUrl of characters) {
      await getCharacterName(characterUrl);
    }
  }
}

const movieId = process.argv[2];
getCharactersOfMovie(movieId);
