const mongoose = require('mongoose');

mongoose.Promise = global.Promise;

mongoose.connect('mongodb://localhost:27017/HTBDB', {
    useNewUrlParser: true,
    useCreateIndex: true,
    useUnifiedTopology: true,
});
