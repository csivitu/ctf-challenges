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


app.use('/static', express.static(path.join(__dirname, 'public')));


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
    let token = req.headers['x-access-token'] || req.headers.authorization;

    token = (!token && (process.env.NODE_ENV === 'production')) ? undefined: token || req.query.token;

    if (!token) {
        res.status(401).json({
            success: false,
            message: 'Invalid Token, Headers?',
        });

        return;
    }

    if (token.includes('Bearer ')) {
        token = token.split('Bearer ')[1];
    }

    if (token.includes('bearer ')) {
        token = token.split('bearer ')[1];
    }

    try {
        req.user = jwt.verify(token, process.env.JWT_SECRET);

        next();
    } catch (err) {
        res.status(400).json({
            success: false,
            message: 'Invalid Token, Headers?',
        });
        return;
    }
}



app.get('/admin', decodeJWT, (req, res) => {
    if (req.user.admin !== str_rot13('true')) {
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

    const username = str_rot13(req.user.username);

    if (!admins.includes(username)) {
        res.send('Username not found in admin list.');
        return;
    }

    res.send(`Hey ${username}! Here's your flag: ${str_rot13('csictf{1n_th3_3nd_1t_d0esn\'t_3v3n_m4tt3r}')}`);
});



app.get('/login', (req, res) => {
    res.sendFile(path.join(__dirname, 'public', 'login.html'));    
});



app.post('/login', (req, res) => {
    const { username, password } = req.body;
    const token = signJWT({ username: str_rot13(username), password: str_rot13(password), admin: str_rot13('false') });
    res.setHeader('token', token);
    res.sendFile(path.join(__dirname, 'public', 'dashboard.html'));
});



app.get('/adminNames', (_req, res) => {
    res.redirect('/getFile?file=admins');
});



app.get('/getFile', (req, res) => {
    let { file } = req.query;

    if (!file) {
        res.send(`Param Undefined Error: file=${file}.`);
        return;
    }

    file = file.toString();

    if (file.length > 7) {
        res.send(`File name too big!`);
        return;
    }

    if (file.split('../').length >= 3) {
        res.send('Invalid filename.');
        return;
    }

    const filePath = path.resolve(__dirname, 'public', file);
    res.sendFile(filePath, { dotfiles: 'allow' }, (err) => {
        if (err) res.send('No such file or directory: ' + filePath);
    });
});


app.get('/', (_req, res) => {
    res.sendFile(path.join(__dirname, 'public', 'index.html'));
});
