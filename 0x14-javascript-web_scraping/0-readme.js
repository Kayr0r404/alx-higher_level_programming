#!/usr/bin/node

const fs = require('fs');

function readAndPrintFile (filePath) {
  fs.readFile(filePath, 'utf-8', (err, data) => {
    if (err) {
      console.error(`Error occurred: ${err.message}`);
    } else {
      console.log(data);
    }
  });
}

// Check if the file path is provided as a command-line argument
if (process.argv.length !== 3) {
  console.error('Usage: node script.js <file_path>');
} else {
  const filePath = process.argv[2];
  readAndPrintFile(filePath);
}
