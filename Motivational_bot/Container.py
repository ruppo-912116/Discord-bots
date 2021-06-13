import discord
from Background_process import MyCog

import random
from discord.ext import commands
from Constants import *

# connection to client on discord
client = discord.Client()
bot = commands.Bot("!")

cog = MyCog(bot)
bot.run(Token)

# @client.event
# async def on_ready():
#     print('we have logged in as {0.user}'.format(client))


# @client.event
# async def on_message(message):
#     msg = message.content
#     if message.author == client.user:
#         return
#
#     if msg.startswith('!test'):
#         await message.channel.send("I am triggered dear!!")
#
#     if any(word in msg for word in sadWords):
#         await message.channel.send(random.choice(inspiringReturns))

# client.run(Token)
