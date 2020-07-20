const express = require('express');
const multer = require('multer');
const fs = require('fs');
const unzipper = require('unzipper');

var upload = multer({ dest: '/home/administrator/uploads/zips' })
const router = express.Router();

router.post('/extract', upload.single('zipFile'), (req, res, next) => {
    console.log(req.file);
    fs.createReadStream(req.file.path).pipe(unzipper.Extract({ path: '/home/administrator/uploads/extracts' }));
    res.json({success: true});
});

module.exports = router;
