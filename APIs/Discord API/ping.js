const Discord = require("discord.js");
const client = new Discord.Client();
const prefix = "!";
client.on('ready', () => {
    console.log('I am ready!');
  client.user.setActivity("<activity>", {type : "<type>"});
  });                     //displays as 'type

client.on("message", message => {
    const args = message.content.slice(prefix.length).trim().split(/ +/g);
    const command = args.shift().toLowerCase();
    if (command == "ping") {
        message.reply(`Pong! Client ping is currently ${client.ping}.`);
    }
});
client.on('guildMemberAdd', member => {
    const channel = member.guild.channels.find(ch => ch.name === 'general');
    if (!channel) return;
    channel.send(`Welcome to the server, ${member}`);
  });  //Welcomes new members

// Specify token, see readme.
client.login("<token>");
