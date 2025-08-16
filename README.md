const { Client } = require('whatsapp-web.js');
const qrcode = require('qrcode-terminal');

const client = new Client();

client.on('qr', qr => {
    qrcode.generate(qr, { small: true });
});

client.on('ready', () => {
    console.log('✅ Bug Bot is ready!');
});

client.on('message', message => {
    if (message.body === '!ping') {
        message.reply('Pong!');
    }
});

client.initialize();
