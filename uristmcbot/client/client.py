import collections

import discord

from discord.ext import commands

class Urist_Bot(commands.Bot):
    def __init__(self, *args, command_prefix='&', botname='Urist McBot', buffer_size=10, **kwargs):
        super().__init__(command_prefix=command_prefix, *args, **kwargs)
        self._botname = botname
        self.buffer_size = buffer_size
        self._logbuffer = collections.deque(maxlen=self.buffer_size)
        
    @property
    def raw_logs(self):
        if self.buffer_size != self._logbuffer.maxlen:
            newbuf = collections.deque(maxlen=self.buffer_size)
            newbuf.extend(self._logbuffer)
            self._logbuffer = newbuf
        return self._logbuffer
        
    @property
    def logs(self):
        return '\n'.join(self.raw_logs)
            
    async def on_ready(self):
        print('My circuits gleam!')
        print('=' * 30)
    
    async def on_message(self, message):
        if message.author == self.user:
            return
            
        logval = ('{author}: {msg} (#{chann})'.format(
            author=message.author,
            msg=message.content,
            chann=message.channel
            )
        )
        self.raw_logs.append(logval)
        print(logval)
        #await message.channel.send('Message from {0.author}: {0.content}'.format(message))
        
UristBot = Urist_Bot()

#@UristBot.command()
#async def login(ctx):
#    await UristBot.say('Logged on as {0}!'.format('Urist McBot'))


