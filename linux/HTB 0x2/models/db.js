const mongoose = require('mongoose');

mongoose.Promise = global.Promise;

mongoose.connect('mongodb://web:9EAC744765EA6F26@34.93.37.238:27017/HTBDB', {
    useNewUrlParser: true,
    useCreateIndex: true,
    useUnifiedTopology: true,
});
