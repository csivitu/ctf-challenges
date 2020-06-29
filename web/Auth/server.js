const express = require('express');
const bodyParser = require('body-parser');
const jwt = require('jsonwebtoken');
const path = require('path');

require('dotenv').config();

const app = express();
const PORT = process.env.PORT || 3000;

if (!process.env.JWT_SECRET) {
    console.error('Fatal: JWT_SECRET not defined.');
    process.exit(1);
}



app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());



app.listen(PORT, () => {
    console.log(`Listening on port ${PORT}`);
});



function str_rot13(str) {
    return (str + '').replace(/[a-zA-Z]/gi, function (s) {
        return String.fromCharCode(s.charCodeAt(0) + (s.toLowerCase() < 'n' ? 13 : -13))
    })
}



function signJWT(data) {
    return jwt.sign(data, process.env.JWT_SECRET);
}



function decodeJWT(req, res, next) {
    const token = req.headers['x-access-token'] || req.headers.authorization || req.query.token;

    if (!token) {
        res.status(401).json({
            success: false,
            message: 'Invalid Token',
        });

        return;
    }

    try {
        req.user = jwt.verify(token, process.env.JWT_SECRET);
        next();
    } catch (err) {
        res.status(400).json({
            success: false,
            message: 'Invalid Token',
        });
    }
}



app.get('/admin', decodeJWT, (req, res) => {
    if (req.user.role !== str_rot13('admin')) {
        res.send('Access Denied: You are not an Admin.');
        return;
    }

    const admins = [
        'thebongy',
        'roerohan',
        'namsnath',
        'sudo-nan0-RaySK',
        'theProgrammerDavid',
        'sauravhiremath',
    ];

    if (!admins.includes(str_rot13(req.user.username))) {
        res.send('Username not found in admin list.');
        return;
    }

    // Do something
    res.send('You are an admin!');
});



app.get('/getToken', (req, res) => {
    const { username, password } = req.query;

    if (!username || !password) {
        res.send(`Missing Parameters. username=${username} & password=${password}`);
    }

    res.send(signJWT({ username: str_rot13(username), password: str_rot13(password), role: str_rot13('user') }));
});



app.get('/verifyToken', decodeJWT, (req, res) => {
    if (!!req.user.role) {
        res.send('Valid Token!');
    }
    res.send('Invalid Token. Token must be in `Authorization`.');
});



app.get('/adminNames', (_req, res) => {
    // SQL Injection here

    res.redirect('/getFile?file=admins');
});



app.get('/getFile', (req, res) => {
    let { file } = req.query;

    if (!file) {
        res.send(`Param Undefined Error: file=${file}.`);
        return;
    }

    file = file.toString();

    if (file.includes('../') && file.length > 7) {
        res.send(`File name too big!`);
        return;
    }

    if (file.split('../').length >= 3) {
        res.send('Invalid filename.');
        return;
    }

    res.sendFile(path.resolve(__dirname, 'public', file), { dotfiles: 'allow' });
});



app.get('/', (_req, res) => {
    res.sendFile(path.join(__dirname, 'public', 'index.html'));
});
