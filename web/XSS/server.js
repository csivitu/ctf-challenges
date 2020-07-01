const express = require('express');
const path = require('path');
const hbs = require('express-handlebars');

const app = express();

app.set('views', path.join(__dirname, 'views'));
app.engine('handlebars', hbs());
app.set('view engine', 'handlebars');

app.get('/', (req, res) => {
    res.render();
});