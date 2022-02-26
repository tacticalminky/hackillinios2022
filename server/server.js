const express = require('express');
const express = require('http');
const path = require('path');
const { Telegraf } = require('telegraf');
const { Socket } = require('socket.io');
const fs = require('fs');
const envfile = require('envfile');
require('dotenv').config();

const app = new express();
const server = http.createServer(app);
const socket = new Socket(server);
const bot = new Telegraf(process.env.BOT_TOKEN);

bot.start((ctx) => {
    let parsedFile = envfile.parse('.env');
    parsedFile.BOT_TOKEN = process.env.BOT_TOKEN;
    parsedFile.CHAT_ID = ctx.message.chat.id;
    fs.writeFileSync('./.env', envfile.stringify(parsedFile));
    ctx.reply('Successfully Connected');
});

bot.launch();

app.get('/', (req, res) => {
    res.sendFile(path.join(`${__dirname}/www/index.html`));
});

app.use(express.static(path.join(__dirname, 'www')));

app.post('/', (req, res) => {
    bot.telegram.sendMessage(process.env.CHAT_ID, 'Post recieved');

});

socket.on('connect', (socket) => {
    console.log("Connected to socket");
});

const port = 8000;
server.listen(port, function() {
    console.log(`Server started at http://localhost:${port}`);
});