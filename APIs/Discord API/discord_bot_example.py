#  make sure you have python 3.5.4 or higher
#  By @ofirisakov
try:
	import discord
	from discord.ext import commands
except ImportError:
	print('Please pip install discord')


PREFIX = '!'
TOKEN = ''  # Place token here
bot = commands.Bot(command_prefix=PREFIX)


@bot.event
async def on_ready():
      """
      Prints on_ready.

      Args:
      """
	print('Logged in!')
	print(f'Name: {bot.user.name}')
	print(f'ID: {bot.user.id}')


@bot.command()
async def ping(ctx):
      """
      Send ping message.

      Args:
          ctx: (todo): write your description
      """
	await ctx.send(f'pong! `{int(bot.latency * 1000)}ms`')


bot.run(TOKEN)
