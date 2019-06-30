import collections

import discord

from discord.ext import commands

class UristBot(commands.Bot):
    def __init__(self, *args, command_prefix='&', botname='Urist McBot', buffer_size=10, **kwargs):
        super().__init__(command_prefix=command_prefix, *args, **kwargs)
        self._botname = botname
        self.buffer_size = buffer_size
        self._logbuffer = collections.deque(maxlen=self.buffer_size)
        
    def __str__(self):
        return self._botname
        
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
            
        if message.content.lower().strip().startswith('$wave'):
            author = message.author.split('#')[0]
            await message.channel.send('Hey there {waver}! :wave::skin-tone-1:'.format(waver=author))
        




