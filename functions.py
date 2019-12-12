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
#verif = pickle_verify_account("accountname")
#pickle_add_account(verif)
#pickle_remove_account(verif)
#pickle_diplay_accounts()


# START DISCORD LISTENER -------------------------------------------------------
def discord_listener():
    os.system("./bot.py")

# START TWITTER LISTENER -------------------------------------------------------
def twitter_listener():
    os.system("./script.py")

# COLLECT & PREPARE TWITS ------------------------------------------------------

def get_twits(verif):
    pickle=[]
    if(os.path.exists(verif["account"])):
        os.system("rm "+verif["account"])
    os.system("wget http://twitter.com/"+verif["account"]+" > /dev/null 2>&1 && mv "+verif["account"]+" "+verif["account"]+"1 && cat "+verif["account"]+"1 |grep TweetTextSize >"+verif["account"] +"2 && rm "+verif["account"]+"1 && cat "+verif["account"]+"2 |grep -oP '(?<=>)[^<]*' > "+verif["account"] +" && rm "+verif["account"]+"2")
    with open(verif["account"]) as file:
        data = file.read()
        array=data.split("&nbsp;")
        twits=[]
        for i in range(len(array)):
            twits.append([array[i],0])
        for i in range(len(twits)):
            twits[i][0] = twits[i][0].replace('\n','').replace('\';','\'').replace('&#39','\'').replace('http','\nhttp').replace('…','').replace('#','')
        for i in range(len(twits)):
            if (twits[i][0] != ""):
                pickle.append(twits[i])
        return pickle

# VERIFY TWIT EXIST & ADD TO PICKLE --------------------------------------------

def verify_twits(array):
    if(os.path.exists("twits.db")):
        with open("twits.db", "rb") as db:
            data = pickle.load(db)
            for i in range(len(array)):
                flag = False
                count= 0
                for y in range(len(data)):
                    if (array[i][0] == data[y][0]):
                        flag = True
                if ( flag == False ):
                    data.append(array[i])

    # DB IS NOT CREATED --------------------------------------------------------
    else :
        data=array
        os.system("touch twits.db")
    pickle.dump(data, open( "twits.db", "wb" ))


# DEBUG PICKLE -----------------------------------------------------------------
def debug_pickle(path):
    with open(path, "rb") as db:
        data = pickle.load(db)
        for i in range(len(data)):
            print(data[i])
            print(" ")

#verif = pickle_verify_account("accountname")
#verify_twits(get_twits(verif))
#debug_pickle("twits.db")
