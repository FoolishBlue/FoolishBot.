import discord 
import discord.ext
from discord.ext.commands import slash_command
from discord.ext import commands
from discord.ext.commands import Cog
from discord.ext import bridge
class Member(commands.Cog):
    def __init__(self, bot):
     self.bot = bot

    @bridge.bridge_command(name="membercount", description="Member Count")
    async def membercount(self, ctx,):
        user_count = len([members for members in ctx.guild.members if not members.bot])
        await ctx.send(f'{ctx.guild.name} has {user_count} members')
    
def setup(bot):
   bot.add_cog(Member(bot)) 