const mongoose = require('mongoose');

mongoose.Promise = global.Promise;

// csictf{exp0s3d_sec23ts}
mongoose.connect('mongodb://web:9EAC744765EA6F26@34.93.215.188:27017/HTBDB', {
    useNewUrlParser: true,
    useCreateIndex: true,
    useUnifiedTopology: true,
});
