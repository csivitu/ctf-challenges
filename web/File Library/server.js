const express = require('express');
const fs = require('fs');

const app = express();

const PORT = process.env.PORT || 3000;

app.listen(PORT, () => {
    console.log(`Listening on port ${PORT}`);
});

app.get('/getFile', (req, res) => {
    const { file } = req.query;

    // If file name is undefined
    if (!file) {
        res.send(`file=${file}\nFilename not specified!`);
        return;
    }

    try {
        // If file name has characters like ' ', '/'
        if (file.includes(' ') || file.includes('/')) {
            res.send(`file=${file}\nInvalid filename!`);
            return;
        }
    } catch (err) {
        res.send('An error occured!');
        return;
    }

    // If the length of file is greater than 5
    if (file.length > 5) {
        res.send(`file=${file}\nFilename too large!`);
        return;
    }

    // Check if file type is allowed
    if (!allowedFileType(file)) {
        res.send(`File type not allowed`);
        return;
    }

    const temp = __dirname + '/' + file;

    // If there are multiple file names (comma separated), take the first one.
    const returnedFile = temp.split(',')[0];

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
    if (format == 'js' || format == 'txt') {
        return true;
    }

    return false;
}