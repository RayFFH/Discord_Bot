import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '/')


@client.event
async def on_ready():
    print("Bot is waiting for command")


client.run('token)