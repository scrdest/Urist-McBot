import os
import hug

PROJECT_ROOT = os.path.dirname(__file__)
TOKENPATH = os.path.join(PROJECT_ROOT, 'token.txt')
API_NAME = __name__

API = hug.API(API_NAME)
bot = None

from uristmcbot.api import commands as apicmds
from uristmcbot.api import index

API.extend(hug.API(index.__name__))
API.extend(hug.API(apicmds.__name__))

def main(*args, **kwargs):
    return apicmds.run_bot.interface.cli()
    
if __name__ == '__main__':
    main()
    