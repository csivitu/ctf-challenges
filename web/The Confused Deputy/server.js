const express = require('express');
const path = require('path');

const visitor = require('./visitor');
const app = express();
const PORT = process.env.PORT || 3000;

app.use(express.urlencoded({ extended: true }));
app.use(express.json());

app.use('/static', express.static(path.join(__dirname, 'static')));

app.listen(PORT, () => {
    console.log(`Listening on port ${PORT}`);
})

app.get('/admin', (req, res) => {
    res.sendFile(path.join(__dirname, 'views', 'admin.html'));
});

app.post('/admin', async (req, res) => {
    let { url, color } = req.body;
    url = url.toString();
    color = color.toString();

    if (!url || !color) {
        res.send('Invalid fields');
        return;
    }

    const hostname = process.env.DOMAIN || req.get('host');

    try {
        const success = await visitor(url, hostname, color);
        if (!success) {
            res.send('An error occured while visiting the link!');
            return;
        }
        res.send('Admin visited your link successfully!');
    } catch (err) {
        console.error(err);
        res.send('Unexpected Error.');
    }
});

app.get('/view', (req, res) => {
    res.sendFile(path.join(__dirname, 'views', 'index.html'));
});

app.get('/', (req, res) => {
    res.redirect('/view');
});
