
import discord
from discord.ext import commands



class rickroll(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="rickroll") 
    async def rickroll(self,ctx, member: discord.Member):
        await member.send("https://tenor.com/view/rick-astly-rick-rolled-gif-22755440")
        await ctx.respond(f"{member} was rickrolled.", ephemeral = True)
def setup(bot):
    bot.add_cog(rickroll(bot))
