
import discord
from discord.ext import commands



class rickroll(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="rickroll") 
    async def rickroll(self,ctx, member: discord.Member):
        await member.send("https://images-ext-1.discordapp.net/external/M7gE5_6-Q5502w2fuVGfgLCL9lG-r8XooAErLDxmTCI/https/media.tenor.com/x8v1oNUOmg4AAAPo/rickroll-roll.mp4")
def setup(bot):
    bot.add_cog(rickroll(bot))
