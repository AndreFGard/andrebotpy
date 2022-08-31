
import discord
from discord.ext import commands
import random
import os
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

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
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
async def cool(ctx):
    """Says if a user is cool.
    In reality this just checks if a subcommand is being invoked.
    """
    if ctx.invoked_subcommand is None:
        await ctx.send(f'No, {ctx.subcommand_passed} is not cool')


@cool.command(name='bot')
async def _bot(ctx):
    """Is the bot cool?"""
    await ctx.send('Yes, the bot is cool.')


###################################################################

@bot.command()
async def linux(ctx):
    await ctx.send('Usa Linux boyy')
    await ctx.send(file=discord.File('Tux.svg.png'))

@bot.command()
async def repete(ctx, *args, content='Repetindo'):
    arguments = ' '.join(args) # .join joins tudo de uma lista, tuple ou dict
#    print (arguments)
    await ctx.send(f'{arguments}')
#    print(*args)
#    print(ctx)
  
@bot.command()
async def repeat(ctx, times: int, content='Repetindo...'):
    """!repeat (número de vezes a repetir) palavra """
    for i in range(times):
        await ctx.send(content)
      

@bot.command()
async def sergio(message, description = 'Quantos dias faltam para SERGIO SALES'):
    """Quantos dias faltam para SERGIO SALES"""
    bday = datetime.datetime.today()
    bdayhj = str(datetime.datetime.today().strftime("%j"))
    if bdayhj == '217':
        sergio = 'HOJE É O ANIVERSÁRIO DO SÉRGIO MITO (ou o dia seguinte)'
    elif bdayhj == '218':
        sergio = 'HOJE É O ANIVERSÁRIO DO SÉRGIO MITO (ou o dia seguinte)'
        print(sergio)
    else:
        sergio = 'Hoje não é o aniverśario de serginho. '
        oo= ( (365 - int(bdayhj)) + 217 )
        print(sergio)
        print(oo)
    await message.send(sergio)
    await message.send('ainda faltam {0} dias'.format(oo))


#keep_alive()
TOKEN = 'MTAwMjkzODY1ODQ0NzQyNTYwOA.GGXcbF.uh_ZJ8xD9XeZouXSHZpxfjPjfKBsZay_ChubJA'


bot.run(TOKEN)











