
import discord
from discord.ext import commands

import aiohttp

class github(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="github") 
    async def github(self,ctx):
        await ctx.respond("Github Repo: [Here](<https://github.com/FoolishBlue/FoolishBot.>)")
def setup(bot):
    bot.add_cog(github(bot))
