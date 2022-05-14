# -*- coding: utf-8 -*-
"""
Example discord bot implementation of bravery script
"""
import discord
from discord.ext import commands
import brave_autoload as br

TOKEN = 'add token here'
description = 'Example bot'
bot = commands.Bot(command_prefix='!', description=description)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    br.update_lists() # intial load of bravery data
    print('------')



@bot.command()
async def brave(ctx, name):
    """generate a ultimate bravery setup - !brave name"""
    a,b,c = br.make_team()
    await ctx.send(name)
    await ctx.send('Origin : '+ a)
    await ctx.send('Class  : '+ b)
    await ctx.send('Carry  : '+ c)
