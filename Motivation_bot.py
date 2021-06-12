import discord
import os
import requests
import json
import random
from discord.ext import commands, tasks

# environment variables
Token = os.environ['TOKEN']
ChannelID = os.environ['ChannelMotivation']

# constants
quotesAPI = "https://zenquotes.io/api/random"
sadWords = ["sad", "depressed", "discouraging", "jhyau", "depressing", "bad"]
inspiringReturns = ["Hang in there mate!", "I love you, everything is fine!", "Cheer up Nigga!"]

# client connection that connects to discord
client = discord.Client()
bot = commands.Bot("!")


# helper function to return quotes from the api
def get_quote():
    response = requests.get(quotesAPI)
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return (quote)


# loop task in 60 seconds
@tasks.loop(hours=8)
async def called_once_a_day():
    message_channel = bot.get_channel(int(ChannelID))
    response = get_quote()
    await message_channel.send(response)


@called_once_a_day.before_loop
async def before():
    await bot.wait_until_ready()
    print("Finished waiting")


called_once_a_day.start()


@client.event
async def on_ready():
    print('we have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    msg = message.content
    if message.author == client.user:
        return

    if msg.startswith('!test'):
        await message.channel.send("I am triggered dear!!")

    if any(word in msg for word in sadWords):
        await message.channel.send(random.choice(inspiringReturns))

bot.run(Token)
client.run(Token)
