# File Library

Author: [roerohan](https://github.com/roerohan)

## Description

Express query parsing vulnerability.

## Requirements

- Express.js
- qs package used by Express.js

## Sources

- [server.js](./server.js)
- Deployed website using server.js

```
This is my file library. I don't have a lot of files, but I hope you like the ones I have!
```

## Exploit

This exploit is owing to the `qs` package used by `express` to parse `req.query`. You can send an array instead of a string through the GET params in the following manner:

```ja
/route?words[]=hello&words[]=world
```

This makes the `req.names` in the backend an array: `['hello', 'world']`.

```javascript
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
```

The `/getFile` route is meant to get you a file from the server. But there are certain restrictions. First, you can't have ` `s or `/`s in your file. This prevents path traversal to an extent. 
<br />

Then, it checks that the `file` parameter has a length of less than 5 characters. This will prevent you from accessing a file like `flag.txt`. Then, it checks if the file ends with `js` or `txt`, only then it will allow you to read that file. If all these are satisfied, a `temp` variable is created to get the absolute path in the directory. After that, it checks whether `temp` has `,`s in it, if yes, it takes the first value before the comma, so that it selects the first file if a user passes many comma-separated files.
<br />

So, if we pass `file[]=flag.txt`, it bypasses all the checks except the `allowedFileType()` check, since the length of the array is less than 5, and it does not have an element ` ` or `/`. Now, you can add 2 new elements to the array `.` and `txt`, to the `file` parameter. Then, `temp` becomes `${__dirname}flag.txt,.,txt`, but the `temp.split(',')[0]` takes care of that. Here's the final payload:

```
/getFile?file[]=flag.txt&file[]=.&file[]=txt
```

The flag is:

```
csictf{5h0uld_5tr1ng1fy_th3_p4r4ms}
```
