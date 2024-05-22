#!/usr/bin/node
const fs = require('fs');

const filePath = process.argv[2];
const textToWrite = process.argv[3];

fs.appendFile(filePath, textToWrite, 'utf8', (err) => {
  if (err) {
    console.error('Error writing to the file:', err);
  }
});
