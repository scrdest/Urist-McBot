import os

def Print(*args, **kwargs):
    return print(*args, **kwargs)

def get_token():
    token = os.environ.get('DISCORD_TOKEN', NotImplemented)
        
    if token is NotImplemented: # empty string is technically valid
        from app import TOKENPATH
        with open(TOKENPATH) as tokenfile:
            try: token = tokenfile.read()
            finally: pass
            
    if token is NotImplemented:
        return ("Token not found!")
        
    return token