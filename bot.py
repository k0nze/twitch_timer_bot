#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__      = "Konstantin (k0nze) Lübeck"
__copyright__   = "Copyright 2020, Twitch Count Bot"
__credits__     = ["NinjaBunny9000: https://github.com/NinjaBunny9000/barebones-twitch-bot"]

__license__     = "BSD 3-Clause License"
__version__     = "0.1"

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
    'Called once when the bot goes online.'
    print(f"{BOT_NICK} is online!")
    ws = bot._ws  # this is only needed to send messages within event_ready
    await ws.send_privmsg(CHANNEL, f"/me has landed!")


@bot.event
async def event_message(ctx):
    'Runs every time a message is sent in chat.'

    # make sure the bot ignores itself and the streamer
    if ctx.author.name.lower() == BOT_NICK.lower():
        return

    await bot.handle_commands(ctx)


@bot.command(name='count')
async def test(ctx):
    count = get_count()
    await ctx.send(f'count {count}')


@bot.command(name='add')
async def test(ctx):
    await ctx.send('added')


@bot.command(name='sub')
async def test(ctx):
    await ctx.send('subtracted')


def get_count():
    with open(JSON_FILE) as json_file:
        data = json.load(json_file)
        return data['count']

def update_count():
    pass

if __name__ == "__main__":
    bot.run()
