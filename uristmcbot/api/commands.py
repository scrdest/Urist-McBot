import sys

import hug

import app

@hug.cli()
@hug.local()
def setup_bot(*args, **kwargs):
    from uristmcbot.client import UristBot as bot_type
    bot = bot_type(*args, **kwargs)
    return bot
    
@hug.get(urls={'/run'})
@hug.cli()
@hug.local()
def run_bot(bot=None, token=NotImplemented):
    rvals = []
    
    _token = token
    if _token is NotImplemented:
        from uristmcbot.utils.general import get_token
        _token = get_token()
        
    _bot = bot or setup_bot()
    app.bot = _bot
    
    try: 
        app.bot.run(_token)
    except Exception as E: 
        sys.excepthook(*sys.exc_info())
        rvals.append("Bot died with exception: {}".format(E))
    else: 
        rvals.append('Bot has ran successfully.')
    
    return rvals
    
