#!/usr/bin/python3
import discord
from discord.ext import commands
from random import randint, choice, shuffle, sample
import math
import sys
from sys import argv
from cmath import cos
from os import environ
import json
import datetime
from resources import words5, wordleClass
from requests import get

description = """An example bot to showcase the discord.ext.commands extension
module.
There are a number of utility commands being showcased here."""
intents = discord.Intents.default()
intents.members = True
intents.message_content = True
bot = commands.Bot(command_prefix="!", description=description, intents=intents)
client = discord.Client(intents=intents)

import Andrebot
import asyncio

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")
    await bot.change_presence(activity=discord.Game("Votando 13"))
    print("------")


andrebot = Andrebot.Andrebot(bot.command, discord)
asyncio.run(andrebot.create_functions())


try:
    BOT_TOKEN = environ["BOT_TOKEN"]
except KeyError:
    print("No BOT_TOKEN env var provided")

bot.run(BOT_TOKEN)
