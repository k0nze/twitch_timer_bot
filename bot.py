#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__      = "Konstantin (k0nze) Lübeck"
__copyright__   = "Copyright 2020, Twitch Count Bot"
__credits__     = ["NinjaBunny9000: https://github.com/NinjaBunny9000/barebones-twitch-bot"]

__license__     = "BSD 3-Clause License"
__version__     = "0.1"
__contact__     = {
                    "Twitch": "https://twitch.tv/k0nze",
                    "Youtube": "https://youtube.com/k0nze",
                    "Twitter": "https://twitter.com/k0nze_gg",
                    "Instagram": "https://instagram.com/k0nze.gg",
                    "Discord": "https://discord.k0nze.gg",
                }

import os
import json

from dotenv import load_dotenv
from os.path import join, dirname
from twitchio.ext import commands

dir_path = os.path.dirname(os.path.realpath(__file__))
dotenv_path = join(dir_path, '.env')
load_dotenv(dotenv_path)

# credentials
TMI_TOKEN = os.environ.get('TMI_TOKEN')
CLIENT_ID = os.environ.get('CLIENT_ID')
BOT_NICK = os.environ.get('BOT_NICK')
BOT_PREFIX = os.environ.get('BOT_PREFIX')
CHANNEL = os.environ.get('CHANNEL')

JSON_FILE = 'data.json'


bot = commands.Bot(
    irc_token=TMI_TOKEN,
    client_id=CLIENT_ID,
    nick=BOT_NICK,
    prefix=BOT_PREFIX,
    initial_channels=[CHANNEL]
)


@bot.event
async def event_ready():
    """ Runs once the bot has established a connection with Twitch """
    print(f"{BOT_NICK} is online!")


@bot.event
async def event_message(ctx):
    """ 
    Runs every time a message is sent to the Twitch chat and relays it to the 
    command callbacks 
    """

    # the bot should not react to itself
    if ctx.author.name.lower() == BOT_NICK.lower():
        return

    # relay message to command callbacks
    await bot.handle_commands(ctx)


@bot.command(name='count')
async def test(ctx):
    """
    Runs when the count command was issued in the Twitch chat and sends the 
    current count to the chat
    """
    count = get_count()
    await ctx.send(f'current count {count}')


@bot.command(name='add')
async def test(ctx):
    """
    Runs when the add command was issued in the Twitch chat and adds to the 
    count
    """
    # check if user who issued the command is a mod
    if(ctx.author.is_mod):

        # parse add command
        command_string = ctx.message.content
        # remove '!add' and white space
        command_string = command_string.replace('!add', '').strip()
        # parse int
        value = 0

        try:
            value = int(command_string) 
        except ValueError:
            value = 0

        if value > 0:
            # add to count
            count = get_count()
            count = count + value
            update_count(count)
            await ctx.send(f'updated count to {count}')


@bot.command(name='sub')
async def test(ctx):
    """
    Runs when the add command was issued in the Twitch chat and subtracts from 
    the count
    """
    # check if user who issued the command is a mod
    if(ctx.author.is_mod):

        # parse add command
        command_string = ctx.message.content
        # remove '!add' and white space
        command_string = command_string.replace('!sub', '').strip()
        # parse int
        value = 0

        try:
            value = int(command_string) 
        except ValueError:
            value = 0

        if value > 0:
            # subtract from count
            count = get_count()
            count = count - value
            update_count(count)
            await ctx.send(f'updated count to {count}')


def get_count():
    """ Reads the count from the JSON file and returns it """
    with open(JSON_FILE) as json_file:
        data = json.load(json_file)
        return data['count']


def update_count(count):
    """ Updates the JSON file with count given """
    data = None

    with open(JSON_FILE) as json_file:
        data = json.load(json_file)

    if data is not None:
        data['count'] = count

    with open(JSON_FILE, 'w') as json_file:
        json.dump(data, json_file, sort_keys=True, indent=4)


if __name__ == "__main__":
    # launch bot
    bot.run()
