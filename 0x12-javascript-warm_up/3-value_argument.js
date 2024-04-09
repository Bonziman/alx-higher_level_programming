#!/usr/bin/node
// Check if an argument is provided
if (process.argv[2] == undefined) {
	console.log('No argument');
} else {
	console.log(process.argv[2]);
}
