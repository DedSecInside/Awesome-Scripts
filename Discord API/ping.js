const Discord = require("discord.js");
const client = new Discord.Client();
const prefix = "!";
client.on("message", message => {
    const args = message.content.slice(prefix.length).trim().split(/ +/g);
    const command = args.shift().toLowerCase();
    if (command == "ping") {
        message.reply(`Pong! Client ping is currently ${client.ping}.`);
    }
});

// Specify token, see readme.
client.login("<token>");
