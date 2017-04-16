#!/usr/bin/env python3.4
import discord
import asyncio
import configparser
import datetime
import random
import os

#Get script location
cwd = os.path.dirname(os.path.realpath(__file__))

#Import config file
config = configparser.ConfigParser()
config.read(cwd + "/config.cfg")

token = config.get("configuration", "token")
bot_channel_id = discord.Object(id=config.get("configuration", "bot_channel_id"))
owner_id = discord.User(id=config.get("configuration", "owner_id"))
admin_id = discord.User(id=config.get("configuration", "admin_id"))


client = discord.Client()

    

@client.event
@asyncio.coroutine
def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    yield from client.send_message(bot_channel_id, "This isn't a butt...")
    yield from client.change_presence(game=discord.Game(name='with butts'))

@client.event
@asyncio.coroutine
def on_message(message):
    if message.author == client.user:
        return
    if random.randint(0,50) >= 40:
        words = message.content.split()
        relpacenum = random.randint(1,5)
        replacedwords = 0
        while relpacenum > replacedwords:
            wordnum = random.randint(1,len(words))
            words[(wordnum-1)] = "butt"
            replacedwords = replacedwords+1
        yield from client.send_message(message.channel, " ".join(words))


client.run(token)