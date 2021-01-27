#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__      = "Konstantin (k0nze) Lübeck"
__copyright__   = "Copyright 2021, Twitch Timer Bot"

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
import asyncio
import re

from pathlib import Path
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


@bot.command(name='settimer')
async def on_settimer(ctx):
    """
    Runs when the settimer command was issued in the Twitch chat and sets a 
    timer 
    """
    # check if user who issued the command is a mod
    if(ctx.author.is_mod):
        # parse add command
        command_string = ctx.message.content
        # remove '!sub' and white space
        command_string = command_string.replace('!settimer', '').strip()
        # parse int

        r = re.findall(r'([0-9]+(h|m|s))', command_string)

        seconds = 0

        if len(r) > 0:
            for time in r:
                if time[1] == 'h':
                    value = int(time[0].replace('h', ''))
                    seconds += value*60*60
                elif time[1] == 'm':
                    value = int(time[0].replace('m', ''))
                    seconds += value*60
                elif time[1] == 's':
                    value = int(time[0].replace('s', ''))
                    seconds += value

        if seconds > 0:
            await timer(seconds, ctx)


async def timer(seconds, ctx):
    print(f"timer set to {seconds}")
    await asyncio.sleep(seconds)
    await ctx.send("!timeralert")


if __name__ == "__main__":
    # launch bot
    bot.run()
