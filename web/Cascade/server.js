const express = require('express');
const path = require('path');

const app = express();
const PORT = process.env.PORT || 3000;

app.use('/static', express.static(path.join(__dirname, 'static')));

app.listen(PORT, () => {
    console.log(`Listening on port ${PORT}`);
})

app.get('/view', (req, res) => {
    res.sendFile(path.join(__dirname, 'views', 'index.html'));
});

app.get('/', (req, res) => {
    res.redirect('/view');
});
