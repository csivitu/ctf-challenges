const express = require('express');
const bodyParser = require('body-parser');
const session = require('express-session');
const hbs = require('express-handlebars');
const path = require('path');
const User = require('./models/user');
const adminRouter = require('./routes/admin');
require('./models/db');

const app = express();

const publicFolder = path.join(__dirname, 'public');
app.set('views', publicFolder);
app.engine(
    'html',
    hbs({
        extname: '.html',
        defaultLayout: path.join(publicFolder, 'layouts', 'main'),
        layoutsDir: path.join(publicFolder, 'layouts'),
    }),
);

app.set('view engine', 'html');

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
    res.render('index.html');
});

app.post('/', async (req, res) => {
    const { username, password } = req.body;

    try {
        const user = await User.findOne({ username, password });

        if (!user) {
            res.send(`No user with username: ${username} and password: ${password}.`);
            return;
        }

        req.session.user = username;
        res.redirect('/home');
    } catch {
        res.send('An unexpected error occured.');
    }
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

app.use('/admin', adminRouter);

app.listen(PORT, () => console.log(`Running on port: ${PORT}`));
