from discord.ext import commands
from os import getenv
import traceback
import discord
from datetime import datetime
import sqlite3
import os

bot = commands.Bot(command_prefix='')


#@bot.event
#async def on_command_error(ctx, error):
#    orig_error = getattr(error, "original", error)
#    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
#    await ctx.send(error_msg)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
dbname = os.path.join(BASE_DIR, "spl2.sqlite3")
conn = sqlite3.connect(dbname)
cur = conn.cursor()

def random_buki():
    cur.execute('select name, url from buki ORDER BY RANDOM() limit 1')
    name, url = cur.fetchall()
    return (name, url)

@bot.command()
async def ping(ctx):
    await ctx.message.delete()
    name, url = random_buki(name, url)
    await ctx.send(f"ポンポーン{name}")

@bot.command()
async def ap(ctx, *args):
    api = []
    for val in args:
        api.append(f'https://uniteapi.dev/p/{val}')
    await ctx.send("\n".join(api))

@bot.command()
async def te(ctx):
    embed=discord.Embed(color=0xf7e37e, timestamp=datetime.utcnow())
    embed.add_field(name="スプラシューター", value="いいよ", inline=False)
    embed.set_footer(text = f"Requested by {ctx.author.name}",icon_url=ctx.author.avatar_url)
    
    await ctx.send(embed = embed)


token = getenv('DISCORD_BOT_TOKEN')
bot.run(token)
