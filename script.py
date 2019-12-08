#!/usr/bin/env python3

import discord
import time
import asyncio
from discord.ext import commands
import pickle
import os
import sys
from const import *

print("Twits Gatherer Online")
bot = commands.Bot(command_prefix='#')

@bot.command()
async def start(ctx):
    while True:
        await ctx.send('oooooh')
        time.sleep(60)
        print("someone ping")

bot.run(TOKEN)
