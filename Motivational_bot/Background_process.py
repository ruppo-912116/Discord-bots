from discord.ext import tasks, commands
from Constants import ChannelID
from Get_quotes import get_quote
from Date_conversion_logic import conversion_to_seconds


class MyCog(commands.Cog):
    # constructor function
    def __init__(self, bot):
        self.bot = bot
        self.called_once_a_day.start()

    # cancel background tasks
    def cog_unload(self):
        self.called_once_a_day.cancel()

    # main task to get quote and send it to the channel
    @tasks.loop(seconds=conversion_to_seconds())
    async def called_once_a_day(self):
        message_channel = self.bot.get_channel(int(ChannelID))
        response = get_quote()
        await message_channel.send(response)

    # await for bot to get ready before starting background process
    @called_once_a_day.before_loop
    async def before_called_once_a_day(self):
        await self.bot.wait_until_ready()
        print("Bot ready!")
