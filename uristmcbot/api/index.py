import hug

import app

@hug.cli()
@hug.get(urls={'/'})
@hug.local()
def index(*args, **kwargs) -> str:
    botname = getattr(app.bot, '_botname', None)
    status = "{Bot} {status}.".format(
        Bot = botname or ('<nameless bot>' if app.bot else 'No bots'),
        status = ('operational'),
    )
    return status
            
    
    
    
