#!/usr/bin/env python3
#-------------------------------------------------------------------------------
# Guillaume Zisa
# 2019/12/07
# Functions
# Version 1
#-------------------------------------------------------------------------------
import pickle
import os

account_path = "accounts"
# VERIFY IF ACCOUNT IS IN THE pickle ---------------------------------------------
def pickle_verify_account(account):
    if(os.path.exists("accounts")):
        file = open("accounts", "rb")
        data = pickle.load(file)
        if(account in data):
            return({"exist" : True,"account" : account})
        else:
            return({"exist" : False,"account" : account})
        file.close()
    else:
        return({"exist" : False,"account" : account})

# ADD ACCOUNT IN THE pickle ------------------------------------------------------
def pickle_add_account(verif):
    if(verif["exist"] == False ):
        if(os.path.exists("accounts")):
            data = pickle.load(open( "accounts", "rb" ))
            data.append(verif["account"])
            pickle.dump(data, open( "accounts", "wb" ))
            return "The account",verif["account"] ,"as been added"
        else:
            data=[verif["account"]]
            pickle.dump(data,open( "accounts", "wb" ))
            return "The database has been creater.\nThe account",verif["account"] ,"as been added"
        open( "accounts", "wb" ).close()
    else:
        return("The account already exist")

# REMOVE ACCOUNT FROM THE pickle -------------------------------------------------
def pickle_remove_account(verif):
    if(verif["exist"] == True ):
        if(os.path.exists("accounts")):
            data = pickle.load(open( "accounts", "rb" ))
            data.remove(verif["account"])
            pickle.dump(data, open( "accounts", "wb" ))
            return "The account",verif["account"] ,"as been added"
        else:
            return "The database is not initialized."
    else:
        return("The account already exist")

# DISPLAY ACCOUNT FROM THE PICKLE ----------------------------------------------
def pickle_diplay_accounts():
    if(os.path.exists("accounts")):
        data = pickle.load(open( "accounts", "rb" ))
        for account in data:
            print(account)

# DEBUG FUNCTIONS PICKLE
#verif = pickle_verify_account("li")
#pickle_add_account(verif)
#pickle_remove_account(verif)
#pickle_diplay_accounts()


# START DISCORD LISTENER -------------------------------------------------------
def discord_listener():
    os.system("./bot.py")

# START TWITTER LISTENER -------------------------------------------------------
def twitter_listener():
    os.system("./script.py")
