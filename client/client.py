import discord

from discord.ext import commands as bot

class UristBot(bot.Bot):
    def __init__(*args, **kwargs):
        super(*args, **kwargs)
    
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))
