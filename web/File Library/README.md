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
```

The `/getFile` route is meant to get you a file from the server. But there are certain restrictions. First, you can't have ` `s or `/`s in your file. This prevents path traversal to an extent. 
<br />

Then, it checks that the `file` parameter has a length of less than 5 characters. If not, it takes just the first 5 characters. Then, it checks if the file extension is `js`, `ts`, `cpp`, or `c`, if yes, it allows you to read that file. If all these are satisfied, the path is resolved using `path.resolve()`.
<br />

In the `a.cpp` file, it says `system("cat flag.txt")`, indicating that the flag is present in the same directory in the `flag.txt`. We can pass in an array which passes the first 2 checks. Then it has to check if the `.slice(file.indexOf('.') + 1)`, so the last 2 elements have to be `['.', 'js']`. So, we can try passing `['flag.txt', '.', 'js']`, which makes the path `/home/user/flag.txt,.,js`, which is invalid. However, we can make use of the `path.resolve()`, and the fact that only the first 5 elements are used. If the array becomes `['a', 'b', 'c', 'd', '/../flag.txt', '.', 'js']` (`js` because `txt` is not allowed). So, this passed the file check, because `.slice()` returns `['js']` and `['js'] == 'js'` is true (not used `===`). Now, to get rid of this, we add 4 random elements before the element having `flag.txt`.
<br />

Now, the string upon concatenation will give `${pwd}/a,b,c,d,/../flag.txt` (now you see why we added `/../`), so that it resolves to `${pwd}/flag.txt` because of `flag.txt`. The payload, therefore, is:

```
/getFile?file[]=a&file[]=b&file[]=c&file[]=d&file[]=/../flag.txt&file[]=.&file[]=js
```

The flag is:

```
csictf{5h0uld_5tr1ng1fy_th3_p4r4ms}
```
