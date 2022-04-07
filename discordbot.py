from discord.ext import commands
from os import getenv
import traceback

bot = commands.Bot(command_prefix='')


#@bot.event
#async def on_command_error(ctx, error):
#    orig_error = getattr(error, "original", error)
#    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
#    await ctx.send(error_msg)


@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def ap(ctx, *args):
    api = []
    for val in args:
        api.append(f'https://uniteapi.dev/p/{val}')
    await ctx.send("\n".join(api))

@bot.command()
async def te(ctx):
    embed=discord.Embed(color=0xf7e37e)
    embed.set_author(name="私だ")
    embed.add_field(name="スプラシューター", value="いいよ", inline=False)
    embed.set_footer(text="こんにちわ")
    
    await ctx.send('embed = embed')


token = getenv('DISCORD_BOT_TOKEN')
bot.run(token)
