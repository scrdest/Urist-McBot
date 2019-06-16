import sys
import threading

import hug

import app
from uristmcbot.utils import general as general_utils

KEY_STATUS = 'status'
KEY_ERROR = 'errors'

@hug.cli()
@hug.local()
def setup_bot(*args, **kwargs):
    from uristmcbot.client import UristBot as bot
    return bot
    
    
@hug.get(urls={'/run'}, requires=hug.authentication.basic(hug.authentication.verify('admin', general_utils.check_admin_pass())))
@hug.cli()
@hug.local()
def run_bot(bot=None, token=NotImplemented):
    rvals = {
        KEY_STATUS: [],
        KEY_ERROR: []
    }
    if app.botthread and app.botthread.is_alive():
        rvals[KEY_STATUS].append("Bot already running and currently in an 'alive' state.")
        return rvals
    
    _token = token
    if _token is NotImplemented:
        from uristmcbot.utils.general import get_token
        try: 
            _token = get_token()
        except ValueError as E: 
            sys.excepthook(*sys.exc_info())
            rvals[KEY_ERROR].append("{}".format(E))
        
    _bot = bot or setup_bot()
    app.bot = _bot
    try: 
        app.botthread = threading.Thread(target=lambda: app.bot.run(_token), name='BotThread', daemon=True)
        app.botthread.start()
    #except Exception as E: 
    #    sys.excepthook(*sys.exc_info())
    #    rvals[KEY_ERROR].append("Bot died with exception: {}".format(E))
    finally:
        pass
    
    if rvals[KEY_ERROR]:
        rvals[KEY_STATUS].append('An error has occured! See field `{errkey}` for details.'.format(errkey=KEY_ERROR))
    else: 
        rvals[KEY_STATUS].append('The bot has ran successfully.')
    
    return rvals
    
