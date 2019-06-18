import sys
import threading

import hug

from uristmcbot.utils import general as general_utils

try: import app
except ImportError: general_utils.Print('Warning: App not running!')

KEY_STATUS = 'status'
KEY_ERROR = 'errors'

@hug.cli()
@hug.local()
def setup_bot(*args, **kwargs):
    from uristmcbot.client import UristBot as bot
    return bot


def _bot_process(bot=None, token=None, rebuild_bot=False):
    import asyncio
    
    bot = (bot if not rebuild_bot else None) or setup_bot()
    
    _token = token
    if not _token:
        try: 
            _token = general_utils.get_token()
        except ValueError as E: 
            sys.excepthook(*sys.exc_info())
            rvals[KEY_ERROR].append("{}".format(E))
        
    if bot.loop and bot.loop.is_running() and not bot.loop.is_closed():
        bot.loop.stop()
        bot.loop.close()
        
    bot.run(_token)
    return
    
@hug.get(urls={'/run'}, requires=hug.authentication.basic(hug.authentication.verify('admin', general_utils.check_admin_pass())))
@hug.cli()
@hug.local()
def run_bot(bot=None, token=NotImplemented):
    rvals = {
        KEY_STATUS: [],
        KEY_ERROR: []
    }
    rvals.update(general_utils.get_endpoints())
    
    if app.botthread and app.botthread.is_alive():
        rvals[KEY_STATUS].append("Bot already running and currently in an 'alive' state.")
        return rvals
    
    _bot = bot or setup_bot()
    app.bot = _bot
    try: 
        app.botthread = threading.Thread(target=_bot_process, args=(app.bot, None), name='BotProcess', daemon=True)
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
    
@hug.get(urls='/logs')
@hug.cli()
@hug.local()
def get_bot_logs(bot=None):
    rvals = {}
    rvals.update(general_utils.get_endpoints())
    bot = bot or app.bot
    if not bot:
        return {KEY_ERROR: 'Bot not initialized!'}
    logs = getattr(bot, 'raw_logs', {'NOT AVAILABLE!'})
    rvals['logs'] = {i: line for i,line in enumerate(logs)}
    return rvals
    
if __name__ == '__main__':
    _bot_process()
    
