
import discord
from discord.ext import commands


class Server(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="serverinfo") 
    async def serverinfo(self, ctx):
             mem = len([mem for mem in ctx.guild.members if not mem.bot])
             Server = discord.Embed(title="Server Statistics", description=f"Server Owner: {ctx.guild.owner}\n Server Name: {ctx.guild.name}\nMember Count: {mem} \n Server Boosts: {ctx.guild.premium_subscription_count}", color = 0x1295db)
             Server.set_footer(text = f"Server ID: {ctx.guild.id}")
             await ctx.respond(embed = Server)

            
def setup(bot):
    bot.add_cog(Server(bot))
