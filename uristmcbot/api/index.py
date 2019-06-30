import hug

import app
import uristmcbot.utils.general as gen_utils

KEY_STATUS = 'status'
KEY_BOT = 'bot'
KEY_THREAD = 'thread'

@hug.cli()
@hug.get(urls={'/', '/index'})
@hug.local()
def index(*args, **kwargs):
    rval = {KEY_STATUS: ('uninitialized' if app.bot is False else 'dead')}
    botname = getattr(app.bot, '_botname', None)
    status = "{Bot} {stat}.".format(
        Bot = botname or ('<nameless bot>' if app.bot else 'No bots'),
        stat = ('operational'),
    )
    rval[KEY_STATUS] = status
    rval.update(gen_utils.get_endpoints())
    
    if app.bot: rval[KEY_BOT] = {str(k): str(v) for k,v in vars(app.bot).items()}
    #if app.botthread: rval[KEY_THREAD] = {str(k): str(v) for k,v in vars(app.botthread).items()}
    return rval
            
    
    
    
