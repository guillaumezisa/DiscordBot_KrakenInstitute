#!/usr/bin/env python3
#-------------------------------------------------------------------------------
# Guillaume Zisa
# 2019/12/07
# Executable of the bot discord
# Version 1
#-------------------------------------------------------------------------------

from functions import *
import argparse
import os
import threading
import time

# COMMAND LINE OPTIONS ---------------------------------------------------------
parser = argparse.ArgumentParser()
parser.add_argument('-a', action='store', dest='add',
                    help='Add a twitter account')
parser.add_argument('-r', action='store', dest='remove',
                    help='Remove a twitter account')
parser.add_argument('-l', action='store_true', default=False, dest='list',
                    help='List all the twitter accounts')
parser.add_argument('-s', action='store_true', default=False, dest='start',
                    help='Start the bot')
results = parser.parse_args()

# COMMAND LINE OPTIONS DEBUG ---------------------------------------------------
#print(' add', results.add, '\n','remove', results.remove, '\n','list', results.list, '\n', 'start', results.start)

# COMMAND LINE TRAITMENT -------------------------------------------------------
if (results.add != None):
    verif = pickle_verify_account(results.add)
    print(pickle_add_account(verif))
if (results.remove != None):
    verif = pickle_verify_account(results.remove)
    print(pickle_remove_account(verif))
if (results.list == True):
    pickle_diplay_accounts()
if (results.start == True):
    thread_discord = threading.Thread(None, discord_listener)
    thread_discord.start()
    time.sleep(1)
    thread_twitter = threading.Thread(None, twitter_listener)
    thread_twitter.start()
