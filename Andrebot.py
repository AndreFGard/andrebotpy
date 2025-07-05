#!/usr/bin/python3
from random import randint, choice, shuffle, sample
import random
import math
import sys
from sys import argv
from cmath import cos
from os import environ
import json
import datetime
import discord.ext
import discord.ext.commands
from resources import words5, wordleClass, Distinction, isocode_to_gentile, AndrebotModel
from resources import detect as lang_detection
from requests import get
import discord



class andrebot_message:
    def __init__(self, data:dict):
        self.data = data

class Interface:
    def __init__(self, api):
      ...

class Discord_Interface:
    """this interface converts whatever api is being used to an api that provides for each function
    a context argument, through which it's possible to obtain any informations relative to the context
    of the message, as well as answer any incoming messages"""
    def __init__(self, decorator):
        self.decorator = decorator

    def interface_middleware_decorator(self, extra_commands=[]):
        def decor(f):
            @self.decorator(name=f.__name__)
            async def f2(ctx, *args):
                if not args: args = []
                try:
                #args = type_cast_args(args)
                    return await f(ctx, *args)
                except Exception as e:
                    await ctx.send(f"Um erro selvagem aconteceu: {e.__str__()}")
        return decor



def type_cast_args(args:list[str]) -> None:
    return [(int(el) if el.isdecimal() else el)  for el in args]

class Andrebot:
    def __init__(self, declarator, interface_cls: type = Discord_Interface, filesPath="./", platform='dsc'):
        self.distinction = Distinction()
        self.emojiappended = ('😀', ' ', '😃', '😄', '😁', '😆', '😅', '😂', '🤣', '🥲', '☺', '️', '😊', '😇', '🙂', '🙃', '😉', '😌', '😍', '🥰', '😘', '😗', '😙', '😚', '😋', '😛', '😝', '😜', '🤪', '🤨',
                        '🧐', '🤓', '😎', '🥸', '🤩', '🥳', '😏', '😒', '😞', '😔', '😟', '😕', '🙁',
                        '☹', '😣', '😖', '😫', '😩', '��', '😢', '😭', '😤', '😠', '��', '🤬', '🤯', '😳', '🥵', '��', '😱', '😨', '😰', '😥', '��', '🤗', 
                        '🤔', '🤭', '🤫', '��', '😶', '😐', '😑', '😬', '��', '😯', '😦', '😧', '😮', '��', '🥱', '😴', '🤤', '😪', '��', '🤐', '🥴', '🤢', '🤮', 
                        '��', '😷', '🤒', '🤕', '🤑', '��', '😈', '👿', '👹', '👺', '��', '💩', '👻', '💀', '☠', '👽', '👾', '🤖', '🎃', '😺', '😸', '😹', '😻', '😼', 
                        '😽', '🙀', '😿', '😾')
        self.filesPath = filesPath
        self.funny_cities = open(self.filesPath+"funny_cities.txt").readlines()
        from toxingar import curses
        self.curses = curses
        self.gabaritoh = open(self.filesPath+"2022_D1.txt").readlines()
        self.gabaritoe = open(self.filesPath+"2022_D2.txt").readlines()

        # Integrate AndrebotModel for local DB
        self.model = AndrebotModel()

        # Use wordleClass without remote API (local only)
        # Pass the model to wordleClass for DB integration
        self.wordle5 = wordleClass(5, words5, platform=platform, model=self.model)

        interface_instance = interface_cls(declarator)
        self.declarator = declarator
        self.dec = interface_instance.interface_middleware_decorator

    async def create_functions(self):
        @self.dec()
        async def add(context, left: int, right: int):
            """Adds two numbers together."""
            return await context.send(sum(map(int, (left, right,))))


        @self.dec()
        async def roll(context, dice: str):
            """Rolls a dice in NdN format."""
            try:
                rolls, limit = map(int, dice.split("d"))
            except Exception:
                return await context.send("Format has to be in NdN!")
                return

            result = ", ".join(str(randint(1, limit)) for r in range(rolls))
            return await context.send(result)
        
        @self.dec()
        async def choose(context, *choices: str):
            """Chooses between multiple choices."""
            return await context.send(choice(choices))
            


        @self.dec()
        async def joined(context, member):
            """Says when a member joined."""
            return await context.send("comando desativado")
            return await context.send(f"{member.name} joined {discord.utils.format_dt(member.joined_at)}")



        ######################################################

        @self.dec()
        async def linux(context):
            """Usa Linux boyy (?)"""
            await context.send("Usa Linux boyy")
            # File sending not implemented in this interface, so just send the message
            # If you want to send a file, implement file sending in the interface
            # return await context.send(file=self.interface.File("Tux.svg.png"))


        @self.dec()
        async def desculpa(context):
            """Peço desculpas pelo meu comportamento uwu"""
            return await context.send("Peço desculpas pelo meu comportamento uwu")

        def get_ofense():
            return choice(self.curses)
        

        @self.dec()
        async def repete(context, *args: list[str], content="Repetindo"):
            """ " !repete palavras a serem repetidas uma vez"""
            times = 1
            if args and isinstance(args[0], str) and args[0].isnumeric():
                times = int(args[0])
                args = args[1:]
            arguments = " ".join(map(str, args))
            if times <= 8:
                return await context.send((f"{arguments}\n" * times))
            else:
                await context.send(f"Pq vc não fala {content} pro seu birolho {times} vezes?")
                t = f"Tá querendo me banir do discord seu {get_ofense()}"
                await context.send(t)
            

        @self.dec()
        async def repeat(context, times: int, content="Repetindo..."):
            """!repeat (número de vezes a repetir) palavra"""
            if times <= 8:
                for i in range(times):
                    await context.send(content)
            else:
                await context.send(f"Pq vc não fala {content} pro seu birolho {times} vezes?")
                return await context.send(f"Tá querendo me banir do discord seu {get_ofense}")


        #        response= requests.get(request_url)
        #         return await context.send(xingada)


        @self.dec()
        async def pizza(context, left: int, right: int, content="Pizzaiando"):
            """!pizza numerodefatias raiodapizza
            use pizzahelp em caso de dúvidas
            """
            fatias = int(left)
            r = int(right)

            b = math.radians((360 / int(fatias)) * 0.5)
            cossenus = cos(b).real
            profundidade = round(r - (cossenus * r), 3)

            senus = math.sin(b).real
            comprimento = round(2 * senus * r, 2)
            print(comprimento)
            return await context.send(comprimento)

        @self.dec()
        async def pizzahelp(context):
            """instrucoes sobre o comando pizza"""
            saida = "Posicione a régua de forma tangente à borda da pizza. Depois, aproxime o ponto de tangência ao centro\
                da circunferencia até que o comprimento do segmento da régua que está \"dentro\" da pizza seja igual ao comprimento\
                    fornecido pelo comando pizza. Inicie dois cortes a partir dos 2 pontos onde a borda da régua intercepta a circunferência.\
                        Agora você tem um pedaço que mede exatamente o necessário!"
            context.send(saida)

        @self.dec()
        async def sergio(context, description="Quantos dias faltam para SERGIO SALES"):
            """Quantos dias faltam para SERGIO SALES"""
            today = int(datetime.datetime.today().strftime("%j"))
            if today == 217 or today == 218:
                sergio = "HOJE É O ANIVERSÁRIO DO SÉRGIO MITO (ou o dia seguinte)"
                await context.send(sergio)
                return
            else:
                sergio = "Hoje não é o aniverśario de serginho. "
                if today > 217:
                    daysuntil = 365 - today + 217
                else:
                    daysuntil = 217 - today
                await context.send(sergio)
                return await context.send(f"ainda faltam {daysuntil} dias")


        @self.dec()
        async def enem(context):
            """Quantos dias faltam pro tinhoso dia (motivacional)"""
            today = int(datetime.datetime.today().strftime("%j"))
            if today == 317:
                return await context.send(f"Hoje é o dia do enem :) {self.emojiappended[randint(1, 116)]}")
            else:
                return await context.send(
                    f"Faltam {317-today} dias pro ENEM {self.emojiappended[randint(1, 116)]}"
                )


        @self.dec()
        async def salve(context, *args):
            tosend = random.choice(self.emojiappended)
            return await context.send(f"Salve pra {random.choice(self.funny_cities)}{tosend}")


        @self.dec()
        async def corrige(context, left: int, mid: str, right: int, content="Corrigindo"):
            """!corrige o enem 2022: dia-enem(1 ou 2) cor(az(azul), br(branco) etc) questão"""
            # arguments = ' '.join(args) # .join joins tudo de uma lista, tuple ou dict
            # cor = arguments[0]   BOT_TOKEN = environ["BOT_TOKEN"]

            # quest = arguments[2]
            # quest2 = arguments[3]
            # questf = ''.join(arguments)
            print(left, mid, right)
            if left == 1:
                if mid == "az":
                    return await context.send(self.gabaritoh[right])
                elif mid == "am":
                    return await context.send(self.gabaritoh[right + 91])
                elif mid == "br":
                    return await context.send(self.gabaritoh[right + 182])
                elif mid == "ro":
                    return await context.send(self.gabaritoh[right + 273])
                else:
                    return await context.send(
                        "sintaxe: !corrige dia-do-enem(1 ou 2) cor-do-caderno(az(de azul), br(de branco), ro(rosa), am(amarelo)) questão"
                    )
            elif left == 2:
                if mid == "am":
                    return await context.send(self.gabaritoe[right])
                elif mid == "cz":
                    return await context.send(self.gabaritoe[right + 1])
                elif mid == "az":
                    return await context.send(self.gabaritoe[right + 92])
                elif mid == "ro":
                    return await context.send(self.gabaritoe[right + 183])
                else:
                    return await context.send(
                        "sintaxe: !corrige dia-do-enem(1 ou 2) cor-do-caderno(az(de azul), br(de branco), ro(rosa), am(amarelo)) questão"
                    )
            else:
                return await context.send(
                    "sintaxe: !corrige dia-do-enem(1 ou 2) cor-do-caderno(az(de azul), br(de branco), ro(rosa), am(amarelo)) questão"
                )
                return await context.send("exemplo: dia 1, prova azul, questão 30: !corrige 1 az 30")


        @self.dec()
        async def nota(context, n1: float, n2: float, n3: float):
            """!nota nota1 nota2 nota3. outputa a nota faltando"""
            n4 = 28 - n1 - n2 - n3
            return await context.send(n4)


        @self.dec()
        async def wordle(context, wordsize = 5):  
            if wordsize not in (5,):
                context.send("Só há suporte para 5 letras")
            return await context.send(self.wordle5.update())
            #async for message in context.history(limit=7):
            #    print(f"{message.author}:  {message.content}")

        @self.dec()
        async def wt(context, guess="NULL"):
            """wt(ordle try) guess"""
            return await context.send(self.wordle5.attempt(guess, context.message.author.name))
                
        @self.dec()
        async def wordlewinners(context):
            """Mostra o ranking dos maiores vencedores do wordle"""
            winners = self.model.get_rank(10)
            if not winners:
                return await context.send("Nenhum vencedor encontrado ou erro de conexão com o banco de dados.")
            msg = "🏆 **Wordle Winners** 🏆\n"
            for i, user in enumerate(winners, 1):
                username = user.get('username') or user.get('anon_username') or 'anon'
                wins = user.get('wins', 0)
                platform = user.get('platform', '')
                msg += f"{i}. {username} ({platform}) — {wins} vitórias\n"
            await context.send(msg)
        
        @self.dec()
        async def lang(ctx, *args):
            dlang = lang_detection(" ".join(map(str, args)))
            return await ctx.send(f"This is how you would look like if you were {isocode_to_gentile[dlang]} or {random.choice(self.funny_cities).replace(' ', '-')[:-1]}ese")
        
        def getDuplas(*pessoas):
            """pessoas's len must be even"""
            people_n = len(pessoas)
            people_shuffled = sample(pessoas, people_n)
            for i in range(0, people_n//2, 2):
                print(str(people_shuffled[i]),str( people_shuffled[i+1]))
            
        # 🄰 🄱 🄲 🄳 🄴 🄵 🄶 🄷 🄸 🄹 🄺 🄻 🄼 🄽 🄾 🄿 🅀 🅁 🅂 🅃 🅄 🅅 🅆 🅇 🅈 🅉
        #Ⓐ Ⓑ Ⓒ Ⓓ Ⓔ Ⓕ Ⓖ Ⓗ Ⓘ Ⓙ Ⓚ Ⓛ Ⓜ Ⓝ Ⓞ Ⓟ Ⓠ Ⓡ Ⓢ Ⓣ Ⓤ Ⓥ Ⓦ Ⓧ Ⓨ Ⓩ 🅐 🅑 🅒 🅓 🅔 🅕 🅖 🅗 🅘 🅙 🅚 🅛 🅜 🅝 🅞 🅟 🅠 🅡 🅢 🅣 🅤 🅥 🅦 🅧 🅨 🅩
        #🅰 🅱 🅲 🅳 🅴 🅵 🅶 🅷 🅸 🅹 🅺 🅻 🅼 🅽 🅾 🅿 🆀 🆁 🆂 🆃 🆄 🆅 🆆 🆇 🆈 🆉 🇦 🇧 🇨 🇩 🇪 🇫 🇬 🇭 🇮 🇯 🇰 🇱 🇲 🇳 🇴 🇵 🇶 🇷 🇸 🇹 🇺 🇻 🇼 🇽 🇾 🇿


        def arrange_groups(persons):
            """returns groups (keys are one and values another) as string and as dict. persons's len must be even."""
            NumOfpersons = len(persons)
            persons.append("Com seus pensamentos")
            Pairs = {}
            i = 0

            while i < NumOfpersons:
                Pairs[persons[i]] = persons[i + 1]
                i += 2
            Output = ""
            i = 1
            for person, pair in Pairs.items():
                Output += f"{i}:   {person} - {pair}\n"
                i += 1
            return Output, Pairs    


        @self.dec()
        async def sortduplas(context, *args):
            """Arranja todos os parametros em duplas, pares e grupos"""
            persons = list(args)
            NumOfpersons = len(persons)
            if NumOfpersons == 0:
                return await context.send("0 duplas")
            shuffle(persons)

            pairs,x = arrange_groups(persons)
            await context.send(pairs)

        @self.dec()
        async def sortgenderedgroups(context, *args):
            """Tries to arrange groups of people with the same gender, or pairs with opposite genders."""
            persons = list(args)
            NumOfpersons = len(persons)
            if NumOfpersons == 0:
                return await context.send("0 duplas")
            
            #arrange persons by gender
            shuffle(persons)
            persons = sorted(persons, key=lambda p: self.distinction.find_gender(p), reverse=True)

            persons.append("com seus pensamentos")
            pairs = "\n".join([(f"{persons[i]} | {persons[NumOfpersons//2 + i]}") for i in range(0, NumOfpersons//2) ])
            await context.send(pairs)


        @self.dec()
        async def gender(context: discord.ext.commands.Context, sender_name=""):
            target_name = sender_name
            if not sender_name:
                sender_name = context.author.name
                target_name = "você"

            gender = self.distinction.find_gender(sender_name.upper())
            if gender == "F":
                return await context.send(f"Eu acho que {target_name} é mulher")
            elif gender == "M":
                return await context.send(f"Eu acho que {target_name} é homem")
            else:
                return await context.send(f"Eu acho que {target_name} é {gender}")