#!/usr/bin/env python3

import discord
from time import *
import asyncio
from discord.ext import commands
import pickle
import os
import sys
from const import *

print("Bot Online")
bot = commands.Bot(command_prefix='#')

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def start(ctx):
    await ctx.send('start')

@bot.command()
async def mondieumasecu(ctx):
    await ctx.send('Je vous absous mon enfant')

bot.run(TOKEN)
