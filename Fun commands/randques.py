
import discord
from discord.ext import commands
import random
import aiohttp

class Randomq(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="meme") 
    async def meme(ctx):
        meme = discord.Embed(title="meme", description="test")

        async with aiohttp.ClientSession() as cs:
            async with cs.get('https://www.reddit.com/r/dankmemes/new.json?sort=hot') as r:
                res = await r.json()
            meme.set_image(res['data']['children'] [random.randint(0, 25)]['data']['url'])
            await ctx.respond(embed=meme)
def setup(bot):
    bot.add_cog(Randomq(bot))
