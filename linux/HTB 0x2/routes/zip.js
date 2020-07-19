const express = require('express');
const multer = require('multer');

var upload = multer({ dest: 'uploads/' })
const router = express.Router();

router.post('/extract', upload.single('zipFile'), (req, res, next) => {
    console.log(req.file);
    res.json({success: true});
});

module.exports = router;
