from discord.ext import commands
from os import getenv
import traceback
import discord
from datetime import datetime
import sqlite3
import os
import urllib.request
import json

bot = commands.Bot(command_prefix='')


# @bot.event
# async def on_command_error(ctx, error):
#     orig_error = getattr(error, "original", error)
#     error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
#     await ctx.send(error_msg)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
dbname = os.path.join(BASE_DIR, "spl2.sqlite3")
conn = sqlite3.connect(dbname)
cur = conn.cursor()

def random_buki():
    cur.execute('select name, url from buki ORDER BY RANDOM() limit 1')
    name, url = cur.fetchone()
    return (name, url)

@bot.command()
async def ping(ctx):
    await ctx.message.delete()
    name, url = random_buki()
    await ctx.send(f"ポンポーン{name}")

@bot.command()
async def ap(ctx, *args):
    if (type(ctx.message.channel == discord.DMChannel)
#    await ctx.message.delete()
        api = []
        for val in args:
            api.append(f'https://uniteapi.dev/p/{val}')
        await ctx.send("\n".join(api))

@bot.command(name = "おぶき")
async def buki(ctx):
    await ctx.message.delete()
    name, url = random_buki()
    embed = discord.Embed(title = name, color=0x5f78f7, timestamp=datetime.utcnow())
    embed.set_image(url = url)
    embed.set_footer(text = f"Requested by {ctx.author.name}",icon_url=ctx.author.avatar_url)
    await ctx.send(embed = embed)

@bot.command()
async def tes(ctx):
    await ctx.message.delete()
    req = urllib.request.urlopen('https://spla2.yuu26.com/schedule').read()
    req = json.loads(req.decode('utf-8'))
    gachi = req["result"]["gachi"]
    embed = discord.Embed(title = "ガチマッチ", color=0xfd2008)
    embed.set_thumbnail(url = "https://i.imgur.com/PzitKch.png")
    embed.add_field(name = "Game mode",value = gachi[0]["rule"], inline=False)
    embed.add_field(name = "Maps",value = f'{gachi[0]["maps"][0]}\n{gachi[0]["maps"][1]}', inline=False)
    embed.add_field(name = "Next Game Mode",value = gachi[1]["rule"], inline=False)
    embed.add_field(name = "Next Maps",value = f'{gachi[1]["maps"][0]}\n{gachi[1]["maps"][1]}', inline=False)
    await ctx.send(embed = embed)

token = getenv('DISCORD_BOT_TOKEN')
bot.run(token)
