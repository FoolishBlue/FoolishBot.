from discord.ext.commands import slash_command
from discord.ext import commands
from discord.ext.commands import Cog
import discord
import random
from discord.ext import bridge
class respect(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
  @bridge.bridge_command(name='payrespect',description='Say command')
  async def payrespect(self, ctx,member: discord.Member) -> None:
        pay = f'Press F to pay respect to {member.mention} \nBig F in the chat'
        skull =f':skull: F in the chat for {member.mention}'
        gb = f'Goodbye cruel world.. {member.mention}'
        called = f'Its called respect.. have some! {member.mention}'
        parents = f'Respect your parents *they pay for your* **internet** {member.mention}'
        await ctx.respond(random.choice([pay, skull,gb,called,parents]))
def setup(bot):
  bot.add_cog(respect(bot)) 