import discord
import time
import discord
from discord.ext.commands import Bot
from discord.ext import commands 
import asyncio
import time
import datetime
import urllib3
from html.parser import HTMLParser
from bs4 import BeautifulSoup
import disbotsettings
import urllib.request
import uuid
from googletrans import Translator
import re


LANGUAGES = {
    'af': 'afrikaans',
    'sq': 'albanian',
    'am': 'amharic',
    'ar': 'arabic',
    'hy': 'armenian',
    'az': 'azerbaijani',
    'eu': 'basque',
    'be': 'belarusian',
    'bn': 'bengali',
    'bs': 'bosnian',
    'bg': 'bulgarian',
    'ca': 'catalan',
    'ceb': 'cebuano',
    'ny': 'chichewa',
    'zh-cn': 'chinese (simplified)',
    'zh-tw': 'chinese (traditional)',
    'co': 'corsican',
    'hr': 'croatian',
    'cs': 'czech',
    'da': 'danish',
    'nl': 'dutch',
    'en': 'english',
    'eo': 'esperanto',
    'et': 'estonian',
    'tl': 'filipino',
    'fi': 'finnish',
    'fr': 'french',
    'fy': 'frisian',
    'gl': 'galician',
    'ka': 'georgian',
    'de': 'german',
    'el': 'greek',
    'gu': 'gujarati',
    'ht': 'haitian creole',
    'ha': 'hausa',
    'haw': 'hawaiian',
    'iw': 'hebrew',
    'hi': 'hindi',
    'hmn': 'hmong',
    'hu': 'hungarian',
    'is': 'icelandic',
    'ig': 'igbo',
    'id': 'indonesian',
    'ga': 'irish',
    'it': 'italian',
    'ja': 'japanese',
    'jw': 'javanese',
    'kn': 'kannada',
    'kk': 'kazakh',
    'km': 'khmer',
    'ko': 'korean',
    'ku': 'kurdish (kurmanji)',
    'ky': 'kyrgyz',
    'lo': 'lao',
    'la': 'latin',
    'lv': 'latvian',
    'lt': 'lithuanian',
    'lb': 'luxembourgish',
    'mk': 'macedonian',
    'mg': 'malagasy',
    'ms': 'malay',
    'ml': 'malayalam',
    'mt': 'maltese',
    'mi': 'maori',
    'mr': 'marathi',
    'mn': 'mongolian',
    'my': 'myanmar (burmese)',
    'ne': 'nepali',
    'no': 'norwegian',
    'ps': 'pashto',
    'fa': 'persian',
    'pl': 'polish',
    'pt': 'portuguese',
    'pa': 'punjabi',
    'ro': 'romanian',
    'ru': 'russian',
    'sm': 'samoan',
    'gd': 'scots gaelic',
    'sr': 'serbian',
    'st': 'sesotho',
    'sn': 'shona',
    'sd': 'sindhi',
    'si': 'sinhala',
    'sk': 'slovak',
    'sl': 'slovenian',
    'so': 'somali',
    'es': 'spanish',
    'su': 'sundanese',
    'sw': 'swahili',
    'sv': 'swedish',
    'tg': 'tajik',
    'ta': 'tamil',
    'te': 'telugu',
    'th': 'thai',
    'tr': 'turkish',
    'uk': 'ukrainian',
    'ur': 'urdu',
    'uz': 'uzbek',
    'vi': 'vietnamese',
    'cy': 'welsh',
    'xh': 'xhosa',
    'yi': 'yiddish',
    'yo': 'yoruba',
    'zu': 'zulu',
    'fil': 'Filipino',
    'he': 'Hebrew'
}



bot = commands.Bot("?")
translator = Translator()

x = []
class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        if translator.detect(message.content).lang != "en":
            embed = discord.Embed(title="Translation",color=0xff72b9)
            embed.add_field(name="Original:", value="{0}".format(message.content), inline=False)
            embed.add_field(name="Translation({0} > {1} | Confidence: {2}):".format(LANGUAGES[translator.detect(message.content).lang].upper(),LANGUAGES[translator.translate(message.content).dest].upper(),translator.detect(message.content).confidence), value="{0}".format(translator.translate(message.content).text), inline=False)
            await message.channel.send(embed=embed)
        else:
            search_results = re.finditer(r'\[.*?\]', message.content)
            for item in search_results:
                itm = item.group(0)
                item = item.group(0).lstrip("[")
                item = item.rstrip("]")
                msg = message.content.replace(item," ")
                msg = msg.replace("[ ]"," ")
                embed = discord.Embed(title="Translation",color=0xff72b9)
                embed.add_field(name="Original:", value="{0}".format(message.content), inline=False)
                embed.add_field(name="Translation({0} > {1}):".format(LANGUAGES["en"].upper(),LANGUAGES[item].upper()), value="{0}".format(translator.translate(msg,item).text), inline=False)
                await message.channel.send(embed=embed)
                
        



client = MyClient()
client.run(disbotsettings.token)

