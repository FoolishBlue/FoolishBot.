import discord
import os
import pymongo
from dotenv import load_dotenv
load_dotenv()
from discord.ext import commands


bot = discord.ext.commands.Bot(intents = discord.Intents.all(),command_prefix='f!', activity = discord.Activity(type=discord.ActivityType.playing, name="BennixMC"))
@bot.event
async def on_ready():
    print('I am online')
@bot.event
async def on_application_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.respond(f'This command is on cooldown, Try again in {round(error.retry_after)} seconds')
WrongParam = discord.Embed(title="Missing Argument", description="Missing Argument in this command, you can use /help to find the information on this command.",color=discord.Color.blue())
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, discord.ext.commands.MissingRequiredArgument):
        await ctx.send(embed = WrongParam, )

directories = ["Fun commands", "Utility Commands", "Other"]
for directory in directories:
    for filename in os.listdir(directory):
        if filename.endswith(".py"):
            
          bot.load_extension(f"{directory}.{filename[:-3]}")

bot.run(os.getenv("TOKEN"))