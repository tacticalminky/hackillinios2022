/* server.js */

const express = require('express');
const path = require('path');

const app = new express();

app.get('/', function(request, response) {
    response.sendFile(path.join(`${__dirname}/www/index.html`));
});

app.use(express.static(path.join(__dirname, 'www')));

const port = 8000;
app.listen(port, function() {
    console.log(`Server started at http://localhost:${port}`)
});