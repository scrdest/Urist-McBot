import os
import time

import hug

TICK_DELAY = 10

PROJECT_ROOT = os.path.dirname(__file__)
TOKENPATH = os.path.join(PROJECT_ROOT, 'token.txt')
PASSPATH = os.path.join(PROJECT_ROOT, 'passdb.txt')

API_NAME = __name__

API = hug.API(API_NAME)
bot = False
botthread = False

from uristmcbot.api import commands as apicmds
from uristmcbot.api import index

API.extend(hug.API(index.__name__))
API.extend(hug.API(apicmds.__name__))

def main(*args, **kwargs):
    Done = False
    while not Done:
        try:
            if not (botthread and botthread.running): apicmds.run_bot()
            else: time.sleep(TICK_DELAY)
        except KeyboardInterrupt:
            Done = True
    else:
        print("Bot going to sleep now...")
        
    
if __name__ == '__main__':
    main()
    