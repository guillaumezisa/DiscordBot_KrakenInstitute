#!/usr/bin/env python3

import discord
from time import sleep, strftime
import asyncio
from discord.ext import commands
import pickle
import os
import sys
from const import *
from functions import *
print("Twits Gatherer Online")
bot = commands.Bot(command_prefix='#')

@bot.command()
async def start(ctx):
    print("echo "+strftime("%Y/%m/%d-%H:%M |")+" Start the twitts collect")
    while True:
        if(os.path.exists("accounts")):
            with open("accounts", "rb") as db_account:
                account = pickle.load(db_account)
                for i in range(len(account)):
                    verif = pickle_verify_account(account[i])
                    verify_twits(get_twits(verif))
                    print(strftime("%Y/%m/%d-%H:%M |")+" Collecting "+account[i])
        sleep(20)
        if(os.path.exists("twits.db")):
            with open("twits.db", "rb") as db:
                data = pickle.load(db)
                for i in range(len(data)):
                    if (data[i][1] == 0 ):
                        await ctx.send(data[i][0])
                        data[i][1] = 1
                        print(strftime("%Y/%m/%d-%H:%M |")+" Adding a new twit")
                        sleep(1)
                pickle.dump(data, open( "twits.db", "wb" ))
        sleep(20)

@bot.command()
async def ping(ctx):
    print(strftime("%Y/%m/%d-%H:%M |")+" Someone send a ping")

@bot.command()
async def mondieumasecu(ctx):
    print(strftime("%Y/%m/%d-%H:%M |")+" Someone has bees absouded")

bot.run(TOKEN)
