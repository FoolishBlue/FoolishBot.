
import discord
from discord.ext import commands
DiscordRules = discord.Embed(title="BennixMC Discord Rules", description="1) Treat all members with the respect they deserve \n\n2) Please keep conversations to two languages, dutch and english although you wont be punished for using another \n • You can use translator bot to translate messages from another language \n\n 3) Use an appropriate name, avatar, bio ect \n • This includes about me, profile picture, name, banner and status. \n\n 4) Avoid sending mass messages in a short amount of time \n • This applies to mentions, images, normal text ect \n\n 5) No Promotion/Advertisments \n • Unless you are a creator at BennixMC, feel free to promote your streams in the discord \n\n 6) Dont send your personal information or others \n\n 7) Dont Harras, bully or threaten anyone \n • This includes swearing to a certian extent towards others, arguing over nothing ect \n\n 8) Stricly no racist/homophobic/offensive messages \n • includes images, videos and gifs \n\n 9) Use common sense \n\n10) Follow the discord TOS https://discord.com/terms \n Staff always have the last say, although if you think a staff member has punished you unfairley you can create a support ticket for this to be dealt with.",color=discord.Color.blue())
DiscordRules.set_author(name="BennixMC", icon_url="https://media.discordapp.net/attachments/882647093427195905/1035540310018768956/BennixTransparent.png")
class dcrules(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="dcrules") 
    async def dcrules(self,ctx):
        await ctx.respond(embed=DiscordRules)
def setup(bot):
    bot.add_cog(dcrules(bot))
