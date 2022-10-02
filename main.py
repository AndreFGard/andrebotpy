
import discord
from discord.ext import commands
import random
import math
import sys
from cmath import cos
import os
import json
import datetime
#from webserver import keep_alive


description = '''An example bot to showcase the discord.ext.commands extension
module.
There are a number of utility commands being showcased here.'''


intents = discord.Intents.default()
intents.members = True
intents.message_content = True
bot = commands.Bot(command_prefix='!', description=description, intents=intents)
client = discord.Client(intents=intents)
emojiappended = ['😀', ' ', '😃', '😄', '😁', '😆', '😅', '😂', '🤣', '🥲', '☺', '️', '😊', '😇', '🙂', '🙃', '😉', '😌', '😍', '🥰', '😘', '😗', '😙', '😚', '😋', '😛', '😝', '😜', '🤪', '🤨', '🧐', '🤓', '😎', '🥸', '🤩', '🥳', '😏', '😒', '😞', '😔', '😟', '😕', '🙁', '☹', '😣', '😖', '😫', '😩', '🥺', '😢', '😭', '😤', '😠', '😡', '🤬', '🤯', '😳', '🥵', '🥶', '😱', '😨', '😰', '😥', '😓', '🤗', '🤔', '🤭', '🤫', '🤥', '😶', '😐', '😑', '😬', '🙄', '😯', '😦', '😧', '😮', '😲', '🥱', '😴', '🤤', '😪', '😵', '🤐', '🥴', '🤢', '🤮', '🤧', '😷', '🤒', '🤕', '🤑', '🤠', '😈', '👿', '👹', '👺', '🤡', '💩', '👻', '💀', '☠', '👽', '👾', '🤖', '🎃', '😺', '😸', '😹', '😻', '😼', '😽', '🙀', '😿', '😾']
indtratadas = open("indtratadas.txt").readlines()

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    await bot.change_presence(activity=discord.Game('Votando 13'))
    print('------')


@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)
    await ctx.send(ctx)


@bot.command()
async def roll(ctx, dice: str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)


@bot.command(description='For when you wanna settle the score some other way')
async def choose(ctx, *choices: str):
    """Chooses between multiple choices."""
    await ctx.send(random.choice(choices))





@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')


@bot.group()
async def cool(ctx, *args):
  """Says if a user is cool.
  In reality this just checks if a subcommand is being invoked.
  """
#  await ctx.send(file=discord.File('foraadm1.mp4'))



###################################################################

@bot.command()
async def linux(ctx):
    await ctx.send('Usa Linux boyy')
#    await ctx.send(file=discord.File('Tux.svg.png'))
#   await ctx.send(file=discord.File('fuderadm3.mp4'))

@bot.command()
async def repete(ctx, *args, content='Repetindo'):
    arguments = ' '.join(args) # .join joins tudo de uma lista, tuple ou dict
#    print (arguments)
    await ctx.send(f'{arguments}')
#    await ctx.send(file=discord.File('fuderadm2.mp4'))
#    print(*args)
#    print(ctx)

@bot.command()
async def repeat(ctx, times: int, content='Repetindo...'):
    """!repeat (número de vezes a repetir) palavra """
    for i in range(times):
        await ctx.send(content)

@bot.command()
async def pizza(ctx, left: int, right: int, content='Pizzaiando'):
    """!pizzanum numerodefatias raiodapizza
    use pizzahelp em caso de dúvidas
    """
    fatias= int(left)
    r = int(right)

    b = math.radians((360/int(fatias))*0.5)
    cossenus = cos(b).real
    profundidade = round(r - (cossenus * r), 3)

    senus = math.sin(b).real
    comprimento = round(2 * senus * r, 2)
    print(comprimento)
    await ctx.send(comprimento)
    

@bot.command()
async def sergio(ctx, description = 'Quantos dias faltam para SERGIO SALES'):
    """Quantos dias faltam para SERGIO SALES"""
    bdayhj = str(datetime.datetime.today().strftime("%j"))
    if bdayhj == '217':
        sergio = 'HOJE É O ANIVERSÁRIO DO SÉRGIO MITO (ou o dia seguinte)'
    elif bdayhj == '218':
        sergio = 'HOJE É O ANIVERSÁRIO DO SÉRGIO MITO (ou o dia seguinte)'
        print(sergio)
    else:
        sergio = 'Hoje não é o aniverśario de serginho. '
        faltambday= ( (365 - int(bdayhj)) + 217 )
        print(sergio)
        print(faltambday)
    await ctx.send(sergio)
    await ctx.send('ainda faltam {0} dias'.format(faltambday))

@bot.command()
async def enem(ctx):
  """Quantos dias faltam pro tinhoso dia (motivacional)"""
  hoje = int(datetime.datetime.today().strftime("%j"))
  faltamenem = 317 - hoje
  await ctx.send(f'Faltam {317-hoje} dias pro ENEM {emojiappended[random.randint(1, 116)]}')

@bot.command()
async def salve(ctx, *args):
    tosend = (indtratadas[random.randint(1, 409)])
    await ctx.send(f'Salve pra {tosend}')




#keep_alive()
TOKEN = 'MTAwMjkzODY1ODQ0NzQyNTYwOA.GQux99.WetR7J_cpf8Pf2qtiIMYb0o_MPTNg1Z11QMLs0'


bot.run(TOKEN)











