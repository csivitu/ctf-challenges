const express = require('express');
const path = require('path');
const fs = require('fs');

const app = express();

const PORT = process.env.PORT || 3000;

app.listen(PORT, () => {
    console.log(`Listening on port ${PORT}`);
});

app.get('/getFile', (req, res) => {
    let { file } = req.query;

    // If file name is undefined
    if (!file) {
        res.send(`file=${file}\nFilename not specified!`);
        return;
    }

    try {
        // If file name has characters like ' ', '/', fail.
        if (file.includes(' ') || file.includes('/')) {
            res.send(`file=${file}\nInvalid filename!`);
            return;
        }
    } catch (err) {
        res.send('An error occured!');
        return;
    }

    // Check if file type is allowed.
    if (!allowedFileType(file)) {
        res.send(`File type not allowed`);
        return;
    }

    // If the file name is too long, shorten it.
    if (file.length > 5) {
        file = file.slice(0, 5);
    }

    // Get the path for the file.
    const returnedFile = path.resolve(__dirname + '/' + file);

    // Read file to check if file exists
    fs.readFile(returnedFile, (err) => {
        if (err) {
            if (err.code != 'ENOENT') console.log(err);
            res.send('An error occured!');
            return;
        }

        res.sendFile(returnedFile);
    });
});

app.get('/*', (req, res) => {
    res.sendFile(__dirname + '/index.html');
});

function allowedFileType(file) {
    const format = file.slice(file.indexOf('.') + 1);

    // Allow only `js` and `txt` files.
    if (format == 'js' || format == 'ts' || format == 'c' || format == 'cpp') {
        return true;
    }

    return false;
}