const express = require('express');
const path = require('path');
const { Telegraf } = require('telegraf');
const fs = require('fs');
const envfile = require('envfile');
require('dotenv').config();

const app = new express();
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
    console.log('Post recieved');
    bot.telegram.sendMessage(process.env.CHAT_ID, 'Post recieved');

});

const port = 8000;
app.listen(port, function() {
    console.log(`Server started at http://localhost:${port}`);
});
require('http').createServer(bot.webhookCallback('/secret-path')).listen(3000);