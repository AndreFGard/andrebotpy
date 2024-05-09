#!/usr/bin/python3
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



class andrebot_message:
    def __init__(self, data:dict):
        self.data = data

class Interface:
    def __init__(self):
        ...
    def build_message(message):
        ...
    def command(fun):
        #changeme
        def new_fun(*args, **kwargs):
            return fun
        return new_fun



class Andrebot:
    def __init__(self, declarator, interface: Interface):
        self.interface = interface

        # BASE_URL= "https://xinga-me.appspot.com/api"
        self.emojiappended = ('😀', ' ', '😃', '😄', '😁', '😆', '😅', '😂', '🤣', '🥲', '☺', '️', '😊', '😇', '🙂', '🙃', '😉', '😌', '😍', '🥰', '😘', '😗', '😙', '😚', '😋', '😛', '😝', '😜', '🤪', '🤨',
                        '🧐', '🤓', '😎', '🥸', '🤩', '🥳', '😏', '😒', '😞', '😔', '😟', '😕', '🙁',
                        '☹', '😣', '😖', '😫', '😩', '��', '😢', '😭', '😤', '😠', '��', '🤬', '🤯', '😳', '🥵', '��', '😱', '😨', '😰', '😥', '��', '🤗', 
                        '🤔', '🤭', '🤫', '��', '😶', '😐', '😑', '😬', '��', '😯', '😦', '😧', '😮', '��', '🥱', '😴', '🤤', '😪', '��', '🤐', '🥴', '🤢', '🤮', 
                        '��', '😷', '🤒', '🤕', '🤑', '��', '😈', '👿', '👹', '👺', '��', '💩', '👻', '💀', '☠', '👽', '👾', '🤖', '🎃', '😺', '😸', '😹', '😻', '😼', 
                        '😽', '🙀', '😿', '😾')
        self.funny_cities = open("funny_cities.txt").readlines()
        from toxingar import curses
        self.curses = curses
        # curses is a tuple containing small offenses
        self.gabaritoh = open("2022_D1.txt").readlines()
        self.gabaritoe = open("2022_D2.txt").readlines()

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
            
        self.wordle5 = wordleClass(5, words5, postUrl=postUrl, getUrl=getUrl, testUrl=testUrl, apiHeaders=apiHeaders)

        self.dec = declarator

    async def create_functions(self):
        @self.dec()
        async def add(context, left: int, right: int):
            """Adds two numbers together."""
            return await context.send(left + right)


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
            return await context.send("Usa Linux boyy")
            return await context.send(file=discord.File("Tux.svg.png"))


        @self.dec()
        async def desculpa(context):
            """Peço desculpas pelo meu comportamento uwu"""
            return await context.send("Peço desculpas pelo meu comportamento uwu")


        @self.dec()
        async def repete(context, *args, content="Repetindo"):
            """ " !repete palavras a serem repetidas uma vez"""
            arguments = " ".join(args)  # .join joins tudo de uma lista, tuple ou dict
            #    print (arguments)
            return await context.send(f"{arguments}")


        @self.dec()
        async def repeat(context, times: int, content="Repetindo..."):
            """!repeat (número de vezes a repetir) palavra"""
            if times <= 8:
                for i in range(times):
                    return await context.send(content)
            else:
                return await context.send(f"Pq vc não fala {content} pro seu birolho {times} vezes?")
                ofensa = self.curses[randint(1, 70)]
                return await context.send(f"Tá querendo me banir do discord seu {ofensa}")


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
            today = str(datetime.datetime.today().strftime("%j"))
            if today == "217":
                sergio = "HOJE É O ANIVERSÁRIO DO SÉRGIO MITO (ou o dia seguinte)"
            elif today == "218":
                sergio = "HOJE É O ANIVERSÁRIO DO SÉRGIO MITO (ou o dia seguinte)"
                print(sergio)
            else:
                sergio = "Hoje não é o aniverśario de serginho. "
                if int(today) > 217:
                    daysuntil = 365 - int(today) + 217
                else:
                    daysuntil = 217 - int(today)
                print(sergio)
                print(daysuntil)
            return await context.send(sergio)
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
            tosend = self.emojiappended[randint(1, 409)]
            return await context.send(f"Salve pra {tosend}")


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
            print("message: " + context.author.name)
            return await context.send(self.wordle5.winners())
            
        def getDuplas(*pessoas):
            people_n = len(pessoas)
            people_shuffled = sample(pessoas, people_n)
            for i in range(0, people_n, 2):
                print(str(people_shuffled[i]),str( people_shuffled[i+1]))
            
        # 🄰 🄱 🄲 🄳 🄴 🄵 🄶 🄷 🄸 🄹 🄺 🄻 🄼 🄽 🄾 🄿 🅀 🅁 🅂 🅃 🅄 🅅 🅆 🅇 🅈 🅉
        #Ⓐ Ⓑ Ⓒ Ⓓ Ⓔ Ⓕ Ⓖ Ⓗ Ⓘ Ⓙ Ⓚ Ⓛ Ⓜ Ⓝ Ⓞ Ⓟ Ⓠ Ⓡ Ⓢ Ⓣ Ⓤ Ⓥ Ⓦ Ⓧ Ⓨ Ⓩ 🅐 🅑 🅒 🅓 🅔 🅕 🅖 🅗 🅘 🅙 🅚 🅛 🅜 🅝 🅞 🅟 🅠 🅡 🅢 🅣 🅤 🅥 🅦 🅧 🅨 🅩
        #🅰 🅱 🅲 🅳 🅴 🅵 🅶 🅷 🅸 🅹 🅺 🅻 🅼 🅽 🅾 🅿 🆀 🆁 🆂 🆃 🆄 🆅 🆆 🆇 🆈 🆉 🇦 🇧 🇨 🇩 🇪 🇫 🇬 🇭 🇮 🇯 🇰 🇱 🇲 🇳 🇴 🇵 🇶 🇷 🇸 🇹 🇺 🇻 🇼 🇽 🇾 🇿
        
        @self.dec()
        async def sortduplas(context, *args):
            """Arranja todos os parametros em duplas"""
            Persons = list(args)
            NumOfPersons = len(Persons)
            if NumOfPersons == 0:
                context.send("0 duplas")
            shuffle(Persons)
            Persons.append("Com seus pensamentos")
            Pairs = {}
            i = 0

            while i < NumOfPersons:
                Pairs[Persons[i]] = Persons[i + 1]
                i += 2
            Output = ""
            i = 1
            for person, pair in Pairs.items():
                Output += f"{i}:   {person} com {pair}\n"
                i += 1
            return await context.send(Output)

