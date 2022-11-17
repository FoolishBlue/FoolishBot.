

import discord
from discord.ext import commands

import aiohttp

class say(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="say") 
    @commands.check_any(commands.is_owner())
    async def say(self,ctx,message):
       
        await ctx.respond(message)
def setup(bot):
    bot.add_cog(say(bot))
