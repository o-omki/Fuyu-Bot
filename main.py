import discord
import os
from discord.ext import commands
import asyncio
import requests
from Server import KeepAlive


intents = discord.Intents.default()
bot= commands.Bot(command_prefix = "f!", owner_id = 414066242476048384, intents = intents)
bot.remove_command("help")


@bot.event
async def on_ready():
    botstatus = discord.Status.online
    game = discord.Game("Oh! hi...")
    await bot.change_presence(status = botstatus, activity = game)
    print("it's wildin'")
    cogs = []

    for cog in cogs:
        try:
            bot.load_extension(cog)
            print(f"{cog} loaded successfully")
        
        except Exception:
            print(Exception)

    while bot.is_ready:
        requests.get("")
        await asyncio.sleep(60)


@bot.event
async def on_message(message):
    if message.author == bot.user:
        pass

    await bot.process_commands(message)


KeepAlive()
token = os.environ.get("TOKEN")
bot.run(token, bot = True, reconnect = True)


    
