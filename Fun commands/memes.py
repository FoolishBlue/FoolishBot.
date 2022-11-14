from discord.ext.commands import slash_command
from discord.ext import commands
from discord.ext.commands import Cog
import discord
import random

import aiohttp

from discord.ext import bridge
class meme(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
  @bridge.bridge_command(name='meme', description='meme command',pass_context=True)
  async def meme(self,ctx): 
    await ctx.defer(ephemeral=True)
    async with aiohttp.ClientSession() as cs:
        async with cs.get('https://www.reddit.com/r/memes.json') as r:
            res = await r.json()
            
            await ctx.send(res['data']['children'] [random.randint(0, 25)]['data']['url'])
            await ctx.send('Meme Sent',ephemeral=True)
        





        
        
def setup(bot):
  bot.add_cog(meme(bot)) 
