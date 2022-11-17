import discord
from discord.ext.commands import slash_command
from discord.ext import commands
Other = discord.Embed(title="Utility Information", description="/**help** \n Sends this command that includes information on every command. ")
Fun = discord.Embed(title="Utility Information", description="/**rickroll** (Member) \n Rickrolls member of choice ;) \n /**meme** \n sends meme from reddit \n f!**8ball** (question) \n Predicts awnser to question.")
Utility= discord.Embed(title="Utility Information", description="/**Github** \n Responds with github link for this bot \n /**membercount** \n Responds with member count (non bots) \n /**serverinfo** \n Sends information on the server that the commmand was run in")

class Help(discord.ui.View):

    @discord.ui.select(
        placeholder = "Choose a category",
        min_values = 1, 
        max_values = 1,
        options = [ 
            discord.SelectOption(
                label="Fun Commands",
                description="Click here to see help on the Fun Commands"
            ),
            discord.SelectOption(
                label="Utility Commands",
                description="Click here to see help about Utility Commands"
            ),
           
               discord.SelectOption(
                label="Misc",
                description="Click here to see help about misc commands"
             )
             
            ]
                )
        
    async def select_callback(self, select, interaction): 
         match select.values[0]:
            case "Fun Commands":
             await interaction.response.edit_message(embed=Fun)
            case "Utility Commands":
             await interaction.response.edit_message(embed=Utility)
            case "Misc":
                await interaction.response.edit_message(embed=Other)


class Helpm(commands.Cog):
  def __init__(self,bot):
    self.bot = bot

  @slash_command(name="help",description="Help and Infomation")
  async def help(self,ctx):
    info=discord.Embed(title="FoolishBot Help",url="https://github.com/FoolishBlue/FoolishBot.",description="Hello, I am FoolishBlue's small discord bot made for a fun project to enhance his skills & for some fun :), My prefix is f! some of my commands will use f! but majority are going to be in slash commands, if you use /help you can get some information on me.",color=discord.Color.blue())
    info.set_author(name="FoolishBlue", url="https://github.com/FoolishBlue/FoolishBot.", icon_url="https://cdn.discordapp.com/attachments/1041776995660472320/1042173159778033674/download.png")
    
   
    await ctx.respond(embed=info, view=Help())
def setup(bot):
   bot.add_cog(Helpm(bot)) 