#!/usr/bin/node

const request = require("request");

if (process.argv.length < 3) {
	console.log('Usage: ./script.js/<movie_id>');
	process.exit(1);
}

const filmid = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${filmid}`;

request(url, (err, res, body) => {
	if (err) {
		throw err;
	}

	const actors = JSON.parse(body).characters;
	if (!actors) {
		console.log([]);
		process.exit(1);
	}
	actors.forEach((actor) => {
		request(actor, {json: true}, (err, res, body) => {
			if (err) {
				throw err;
			}
			console.log(body.name);
		});
	});
});
