#!/usr/bin/env python3
import discord
import time
import asyncio
from discord.ext import commands
import pickle
import os

bot = commands.Bot(command_prefix='#')

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def mondieumasecu(ctx):
    await ctx.send('Je vous absous mon enfant')


token = ''
bot.run(token)
