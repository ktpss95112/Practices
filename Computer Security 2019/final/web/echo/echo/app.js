const express = require('express');
const https = require('https');
const fs = require('fs')
const bodyParser = require('body-parser');


const app = express();
app.use(bodyParser.urlencoded({ extended: true }));

app.get('/echo.zip', (req, res) => {
    res.sendfile(`${__dirname}/echo.zip`);
});

app.get('/', (req, res) => {
    res.render('index.ejs');
});

app.post('/', (req, res) => {
    let data = req.body;
    res.render('echo.ejs', data);
});

https.createServer({
    key: fs.readFileSync('server.key'),
    cert: fs.readFileSync('server.cert')
}, app).listen(49007, () => {
    console.log("Listening ...")
})
