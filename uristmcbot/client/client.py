import discord

from discord.ext import commands

UristBot = commands.Bot(command_prefix='&')
UristBot._botname = 'Urist McBot'

@UristBot.command()
async def on_ready(self):
    print('Logged on as {0}!'.format(self.user))

@UristBot.command()
async def on_message(self, message):
    print('Message from {0.author}: {0.content}'.format(message))
