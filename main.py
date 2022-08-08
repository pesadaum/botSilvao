import os
from discord.ext import commands as cmd
from db import db
from server import server_th
import random

TK = os.environ['bot_token']

bot = cmd.Bot(command_prefix='!')


@bot.command(name='baton')
async def baton(ctx):
    await ctx.send('Ba...ton?' +
                   'https://i.ytimg.com/vi/3tQtnzRPm7s/sddefault.jpg')



@bot.command(name='programação')
async def programacao(ctx):
    pics = db.pics_silvao()
    await ctx.send(pics[random.randint(0, len(pics) - 1)])


server_th()
bot.run(TK)
