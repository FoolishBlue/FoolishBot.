
import discord
from discord.ext import commands
MinecraftRules = discord.Embed(title="BennixMC Minecraft Rules", description="1) 1. No greifing on claimed land \n • Unclaimed land CAN be greifed (although not encouraged) \n\n 2) No killing, stealing or looting on claimed land \n • This is also allowed in unclaimed land although not encouraged \n\n 3) No duping or abusing minecraft/server bugs, you will be punished if caught abusing any bugs. \n\n 4) Dont cheat/hack including xray texture packs \n\n5) Follow the discord rules within MC too. (No swearing, bullying, offensive words ect)\n\n 6) Enjoy yourself, Explore the wonders of BennixMC! \n Staff always have the final say, make a discord ticket if you see you've been false punished",color=discord.Color.blue())
MinecraftRules.set_author(name="BennixMC", icon_url="https://media.discordapp.net/attachments/882647093427195905/1035540310018768956/BennixTransparent.png")
class mcrules(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="mcrules") 
    async def dcrules(self,ctx):
        await ctx.respond(embed=MinecraftRules)
def setup(bot):
    bot.add_cog(mcrules(bot))
