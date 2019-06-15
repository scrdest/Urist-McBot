import os
import argparse
import discord

from client import UristBot

PROJECT_ROOT = os.path.dirname(__file__)
TOKENPATH = os.path.join((PROJECT_ROOT, 'token.txt'))

def main(*args, **kwargs);
    bot = UristBot()
    token = None
    with open(TOKENPATH) as tokenfile:
        token = tokenfile.read()
    if not token:
        raise ValueError('Token not found!')
    bot.run(token)
    
if __name__ == '__main__':
    main()
    