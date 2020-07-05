const express = require('express');
const path = require('path');
const cookieParser = require('cookie-parser');

const app = express();

const PORT = process.env.PORT || 3000;

app.use(cookieParser());

app.listen(PORT, () => {
    console.log(`Listening on port ${PORT}`);
});

app.get('/', (req, res) => {
    const cookie = req.cookies.flavour;
    if (cookie === 'Y2hvY29sYXRl') {
        res.send('csictf{1ick_twi5t_dunk}');
        return;
    }
    res.cookie('flavour','c3RyYXdiZXJyeQ==');
    res.sendFile(path.join(__dirname, 'public', 'index.html'));
});
