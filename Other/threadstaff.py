
import discord
from discord.ext import commands

import aiohttp

class thread(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
   
    @commands.Cog.listener()
    async def on_message(self,message):
        if message.webhook_id == 1045793294891896953:
            await message.create_thread(name="Discuss Application", auto_archive_duration=10080)
       


def setup(bot):
    bot.add_cog(thread(bot))
