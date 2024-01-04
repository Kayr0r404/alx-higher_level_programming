#!/usr/bin/node

const fs = require('fs');

function writeToFile (filePath, content) {
  fs.writeFile(filePath, content + '\n', 'utf-8', (err) => {
    if (err) {
      console.error(`Error occurred while writing to ${filePath}: ${err.message}`);
    } else {
      console.log(`Content written to ${filePath}`);
    }
  });
}

// Check if the file path and content are provided as command-line arguments
if (process.argv.length !== 4) {
  console.error('Usage: node script.js <file_path> <content>');
} else {
  const filePath = process.argv[2];
  const content = process.argv[3];
  writeToFile(filePath, content);
}
