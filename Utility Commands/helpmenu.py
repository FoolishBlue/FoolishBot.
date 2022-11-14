# #import discord
# #from discord.ext.commands import slash_command
from discord.ext import commands

# #Utility = discord.Embed(title="Utility Command Help",description="Here is a list of FelBot's Utility related commands along with their infomation\n :arrow_right:  `/ban` - Bans a user and will DM them the reason for their ban \n :arrow_right: `/bean` - Fake bans a member, Bans and unbans with an invite in dms \n :arrow_right: `/github` - Sends the github repo link \n :arrow_right: `/kick` - Kicks a member and sends them reason \n :arrow_right: `/membercount` - Sends the server member count without including bots \n :arrow_right: `/nick` - Changes another members nickname to CensoredNick \n :arrow_right: `/serverinfo` - Sends an embed about the server infomation/stats \n :arrow_right: `/slowmode` - Sets the channel slowmode \n :arrow_right: `/stats` - Sends the server infomation/stats \n :arrow_right: `/howtoverify` - Sends a youtube video showing how to verify with skykings \n :arrow_right: `/help` - Sends infomation about the bot and select menu for help commands \n :arrow_right: `/suggest` - Opens a modal for your suggestion and sends to suggest channel ", color =discord.Color.blue())
# #Fun = discord.Embed(title="Fun Commands Help", description="Here is a list of FelBot's Fun related command and their infomation \n :arrow_right: `/dm` - DM's a member with the message of your choice \n :arrow_right: `/rickroll` - Sends the member a rickroll \n :arrow_right: `/say` - Sends a message of your choice ",color = discord.Color.blue())
# #Embeds = discord.Embed(title="Embeds Help", description="Here is a list of FelBot's Embeds that are run through commands and includes what they do \n :arrow_right: `/apply` - Sends the apply info embed \n :arrow_right: `/BotRules` - Sends FelBot's rules \n :arrow_right: `/perks` - Sends the perks/info of level roles, boosting,staff roles and extra roles \n :arrow_right: `/rules` - Sends felbcord rules   ",color = discord.Color.blue())

 #class Help(discord.ui.View):
    
        

#  #   @discord.ui.select(
#   #      placeholder = "Choose a category",
#    #     min_values = 1, 
#     #    max_values = 1,
#      #   options = [ 
#      #       discord.SelectOption(
#       #          label="Fun Commands",
#        #         description="Click here to see help on the Fun Commands"
#         #    ),
#          #   discord.SelectOption(
#           #      label="Utility Commands",
#            #     description="Click here to see help about Utility Commands"
#             #),
#             #discord.SelectOption(
#              #   label="Embeds Help",
#               #  description="Click here to see help about Embeds"
#             # )
             
#             #]
#                 )
        
#     async def select_callback(self, select, interaction): 
#          match select.values[0]:
#             case "Fun Commands":
#              await interaction.response.edit_message(embed=Fun)
#             case "Embeds Help":
#              await interaction.response.edit_message(embed=Embeds)
#             case "Utility Commands":
#              await interaction.response.edit_message(embed=Utility)


class Helpm(commands.Cog):
   def __init__(self,bot):
     self.bot = bot

#   @slash_command(name="help",description="Help and Infomation")
#   async def help(self,ctx):
#     info=discord.Embed(title="Felbot Infomation",url="https://github.com/VividBlue1/FelBot",description="Hello! I am a personal slave bot who helps around moderating and providing fun into the felbcord! \n If you have any questions about me feel free to ask @ignfoolish#0396 - my creator \n Join Felbcord here! \n https://discord.gg/ab5cxuQu7E \n Feel free to click below if you are needing help with any of my features!",color=discord.Color.blue())
#     info.set_author(name="FelBot", url="https://github.com/VividBlue1/FelBot", icon_url="https://i.ibb.co/tz7VQJw/felb.jpg")
    
   
#     await ctx.respond(embed=info, view=Help())
def setup(bot):
    bot.add_cog(Helpm(bot)) 