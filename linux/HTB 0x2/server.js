const express = require('express');
const bodyParser = require('body-parser');
const session = require('express-session');
const path = require('path');
const User = require('./models/user');
require('./models/db');

const app = express();

app.use(session({
    secret: 'b1gb24int1m3',
    resave: false,
    saveUninitialized: true,
    cookie: { secure: false },
}));

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

const PORT = process.env.PORT || 3000;

app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

app.post('/', async (req, res) => {
    const { username, password } = req.body;
    const user = await User.findOne({ username, password });

    if (!user) {
        res.send(`No user with username: ${username} and password: ${password}.`);
        return;
    }

    req.session.user = username;
    res.redirect('/home');
});

function isLoggedIn(req, res, next) {
    if (!req.session.user) {
        res.redirect('/');
        return;
    }
    next();
}

app.get('/home', isLoggedIn, (req, res) => {
    res.send('HOME!');
});

app.listen(PORT, () => console.log(`Running on port: ${PORT}`));
