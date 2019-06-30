import sys
import asyncio

from uristmcbot.utils import general as general_utils

def _bot_process(bot=None, token=None, rebuild_bot=False):
    bot = (bot if not rebuild_bot else None)
    
    _token = token
    if not _token:
        try: 
            _token = general_utils.get_token()
        except ValueError as E: 
            sys.excepthook(*sys.exc_info())
            rvals[KEY_ERROR].append("{}".format(E))
        
    bot.run(_token)
    return
    