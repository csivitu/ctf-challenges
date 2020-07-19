const express = require('express');
const libxml = require('libxmljs2');
const parser = require('xml2json');
const router = express.Router();

const User = require('../models/user');

function isAdmin(req, res, next) {
    if (req.session.user !== 'admin') {
        res.redirect('/');
        return;
    }
    next();
}

// router.use(isAdmin);

router.get('/', (req, res) => {
    res.render('admin');
});

function xml2json(xml) {
    const data = xml;
    const xmlDoc = libxml.parseXml(data, { noblanks: true, noent: true, nocdata: true })
    const xmlString = xmlDoc.root().toString(false);
    return JSON.parse(parser.toJson(xmlString));
}

router.post('/query', async (req, res) => {
    const { obj, type } = req.body;

    if (type !== 'json' && type !== 'xml') {
        res.render('admin', { template: 'This type is not supported right now. Sorry for the inconvenience.' });
        return;
    }

    let template = '';
    let query = {};

    try {
        if (type === 'json') {
            query = JSON.parse(obj);
        }

        if (type === 'xml') {
            query = xml2json(obj);
        }

        const result = await User.findOne(query);
        if (!result) {
            template = 'Empty';
        } else {
            template += JSON.stringify(result);
        }
    } catch (e) {
        template = e;
    }

    query = JSON.stringify(query);

    res.render('admin', { template, query });
});

module.exports = router;