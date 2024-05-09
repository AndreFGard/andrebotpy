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

# BASE_URL= "https://xinga-me.appspot.com/api"
emojiappended = ('😀', ' ', '😃', '😄', '😁', '😆', '😅', '😂', '🤣', '🥲', '☺', '️', '😊', '😇', '🙂', '🙃', '😉', '😌', '😍', '🥰', '😘', '😗', '😙', '😚', '😋', '😛', '😝', '😜', '🤪', '🤨',
                  '🧐', '🤓', '😎', '🥸', '🤩', '🥳', '😏', '😒', '😞', '😔', '😟', '😕', '🙁',
                  '☹', '😣', '😖', '😫', '😩', '��', '😢', '😭', '😤', '😠', '��', '🤬', '🤯', '😳', '🥵', '��', '😱', '😨', '😰', '😥', '��', '🤗', 
                  '🤔', '🤭', '🤫', '��', '😶', '😐', '😑', '😬', '��', '😯', '😦', '😧', '😮', '��', '🥱', '😴', '🤤', '😪', '��', '🤐', '🥴', '🤢', '🤮', 
                  '��', '😷', '🤒', '🤕', '🤑', '��', '😈', '👿', '👹', '👺', '��', '💩', '👻', '💀', '☠', '👽', '👾', '🤖', '🎃', '😺', '😸', '😹', '😻', '😼', 
                  '😽', '🙀', '😿', '😾')
indtratadas = open("indtratadas.txt").readlines()
from toxingar import curses
# curses is a tuple containing small offenses
gabaritoh = open("2022_D1.txt").readlines()
gabaritoe = open("2022_D2.txt").readlines()

try:
    apiKey = environ["apiKey"] 
    apiHeaders = {'Authorization': apiKey}
    postUrl = environ["postUrl"]
    getUrl = environ["getUrl"]
    global testUrl
    testUrl = environ["testUrl"]
except KeyError:
    print("check apikey, headers, posturl, geturl and testUrl")
    sys.exit(1)
print(f"post url, geturl: {postUrl}, {getUrl}")
testRequest = get(testUrl, headers=apiHeaders)
print(testRequest.text + ":" + str(testRequest.status_code))
if testRequest.status_code != 200:
    sys.exit(1)
wordle5 = wordleClass(5, words5, postUrl=postUrl, getUrl=getUrl, testUrl=testUrl, apiHeaders=apiHeaders)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")
    await bot.change_presence(activity=discord.Game("Votando 13"))
    print("------")


# -generated with a  macro #
#############################################
import Andrebot
andrebot = Andrebot.Andrebot(print)
@bot.command()
async def add(ctx, *args):return await andrebot.add(ctx, *args)
@bot.command()
async def choose(ctx, *args):return await andrebot.choose(ctx, *args)
@bot.command()
async def corrige(ctx, *args):return await andrebot.corrige(ctx, *args)
@bot.command()
async def desculpa(ctx, *args):return await andrebot.desculpa(ctx, *args)
@bot.command()
async def enem(ctx, *args):return await andrebot.enem(ctx, *args)
@bot.command()
async def getDuplas(ctx, *args):return await andrebot.getDuplas(ctx, *args)
@bot.command()
async def print(ctx, *args):return await andrebot.print(ctx, *args)
@bot.command()
async def joined(ctx, *args):return await andrebot.joined(ctx, *args)
@bot.command()
async def linux(ctx, *args):return await andrebot.linux(ctx, *args)
@bot.command()
async def nota(ctx, *args):return await andrebot.nota(ctx, *args)
@bot.command()
async def pizza(ctx, *args):return await andrebot.pizza(ctx, *args)
@bot.command()
async def pizzahelp(ctx, *args):return await andrebot.pizzahelp(ctx, *args)
@bot.command()
async def repeat(ctx, *args):return await andrebot.repeat(ctx, *args)
@bot.command()
async def repete(ctx, *args):return await andrebot.repete(ctx, *args)
@bot.command()
async def roll(ctx, *args):return await andrebot.roll(ctx, *args)
@bot.command()
async def salve(ctx, *args):return await andrebot.salve(ctx, *args)
@bot.command()
async def sergio(ctx, *args):return await andrebot.sergio(ctx, *args)
@bot.command()
async def sortduplas(ctx, *args):return await andrebot.sortduplas(ctx, *args)
@bot.command()
async def wordle(ctx, *args):return await andrebot.wordle(ctx, *args)
@bot.command()
async def wordlewinners(ctx, *args):return await andrebot.wordlewinners(ctx, *args)
@bot.command()
async def wt(ctx, *args):return await andrebot.wt(ctx, *args)
#############################################


try:
    BOT_TOKEN = environ["BOT_TOKEN"]
except KeyError:
    print("No BOT_TOKEN env var provided")

bot.run(BOT_TOKEN)
