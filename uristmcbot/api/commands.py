import sys
import threading
import time
import asyncio

import hug

from uristmcbot.utils import general as general_utils
from uristmcbot.client import botprocess

try: import app
except ImportError: general_utils.Print('Warning: App not running!')

KEY_STATUS = 'status'
KEY_ERROR = 'errors'

@hug.cli()
@hug.local()
def setup_bot(*args, **kwargs):
    from uristmcbot.client import UristBot
    new_bot = UristBot(loop=asyncio.new_event_loop())
    return new_bot
    
@hug.get(urls={'/run'}, requires=hug.authentication.basic(hug.authentication.verify('admin', general_utils.check_admin_pass())))
@hug.local()
@hug.cli()
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
        app.botthread = threading.Thread(target=botprocess._bot_process, args=(app.bot, None), name='BotProcess', daemon=True)
        app.botthread.start()
    #except Exception as E: 
    #    sys.excepthook(*sys.exc_info())
    #    rvals[KEY_ERROR].append("Bot died with exception: {}".format(E))
    finally:
        pass
    
    if rvals[KEY_ERROR]:
        rvals[KEY_STATUS].append('An error has occured! See field `{errkey}` for details.'.format(errkey=KEY_ERROR))
    else: 
        rvals[KEY_STATUS].append('{} has ran successfully.'.format(app.bot))
    
    return rvals
    
@hug.get(urls='/logs')
@hug.cli()
@hug.local()
def get_bot_logs(bot=None):
    rvals = {}
    rvals.update(general_utils.get_endpoints())
    bot = bot or app.bot
    if not bot:
        return {KEY_ERROR: ('Bot not initialized!' if bot is False else 'Bot no longer alive!')}
    logs = getattr(bot, 'raw_logs', {'NOT AVAILABLE!'})
    rvals['logs'] = {i: line for i,line in enumerate(logs)}
    return rvals
    
@hug.get(urls='/kill', requires=hug.authentication.basic(hug.authentication.verify('admin', general_utils.check_admin_pass())))
@hug.cli()
@hug.local()
def kill_bot(bot=None):
    rvals = {}
    bot = bot or app.bot
    rvals[KEY_STATUS] = 'Bot aliv and stronk.' if bot else ('No bots initialized.' if bot is False else 'No bots alive.')
    rvals.update(general_utils.get_endpoints())
    
    if bot:
        asyncio.gather(*asyncio.Task.all_tasks()).cancel()
        bot.loop.stop()
        waits = 0
        while bot.loop.is_running() and waits < 100:
            time.sleep(0.25) # fractions of seconds
            waits += 0
        bot.loop.close()
        bot.clear()
        rvals[KEY_STATUS] = 'Bot killed!'
        app.bot = None
        app.botthread.join()
        app.botthread = None
    return rvals
    
if __name__ == '__main__':
    _bot_process()
    
