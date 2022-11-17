from discord.ext.commands import slash_command
from discord.ext import commands
from discord.ext.commands import Cog
import discord
import random
from discord.ext import bridge
class respect(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
  @commands.command(name='8ball',description='Predict any question.')
  async def _8ball(self,ctx,error,question = None):
    options = ["Nope",
          "Correct",
          "Yes.",
          "I think so",
          "No",
          "Incorrect",
          "Perhaps",
          "I am unsure", 
          "From my POV, I say yes.",
          "Im struggling to predict right now",
          "Im not going to give you an awnser right now, try again."
          "Not convinced"]
    await ctx.send(random.choice(options))

  
  
    
    
def setup(bot):
  bot.add_cog(respect(bot)) 