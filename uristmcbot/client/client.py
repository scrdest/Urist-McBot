import discord

from discord.ext import commands

class UristBot(commands.Bot):
    def __init__(self, *args, **kwargs):
        self._botname = 'Urist McBot'
        super(*args, **kwargs)
        
    def __str__(self):
        return getattr(self, '_botname') or repr(self)
    
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))
