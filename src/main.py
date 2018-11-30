"""
A bot for the Asian Creative Network.
"""

import asyncio
import json

import discord


# configuring the bot using config.json
with open('config.json') as f:
    data = json.load(f)

token = data["token"]
command_prefix = data["prefix"]

client = discord.Client()

check_if_delete_msg(message):
	if message.contains(".role "):
		return True
	else:
		return False

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    """
    When a user in the server sends a message, this checks if a command is sent to the bot.
    If it is for the bot, this will execute the command.
    """
    purge_from(channel, check_if_delete_msg, limit=100, check=None, before=None, after=None, around=None) 
client.run(token)
