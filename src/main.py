"""
A bot for the Asian Creative Network.
"""

import json
import time
import logging

import discord

# configuring the bot using config.json
with open('config.json') as f:
    data = json.load(f)

token = data["token"]
command_prefix = data["prefix"]

delete_these_strings = [".role ",
                        "wtf? role not found, spel teh name beter or something.",
                        "access granted to role ", command_prefix + "clear",
                        "Clearing messages...", ".help", "homepage", ".derole ",
                        "seriously? you already have the", "access removed from role",
                        "invalid command, clearly someone is unable to read the docs"]

client = discord.Client()

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(
    filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter(
    '%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


@client.event
async def on_message(message):
    """
    When a user in the server sends a message, this checks
    if a command is sent to the bot.
    If it is for the bot, this will execute the command.
    """
    for delete_me in delete_these_strings:
        if message.content.startswith(delete_me):
            time.sleep(5)
            await client.delete_message(message)
    if message.content.startswith(command_prefix + 'clear'):
        async for msg in client.logs_from(message.channel, 100):
            for delete_me in delete_these_strings:
                if msg.content.startswith(delete_me):
                    await client.delete_message(msg)


client.run(token)
