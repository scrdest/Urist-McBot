import os

KEY_LINKS = 'available endpoints'

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
        raise ValueError("Token not found!")
        
    return token
    
def get_endpoints(api=None):
    if not api:
        from app import API as app_api
        api = app_api
    
    if hasattr(api, 'http'):
        return {KEY_LINKS: sorted(map(str, api.http.urls()))}
    return {}
    
    
def check_admin_pass():
    adminpass = os.environ.get('API_ADMIN_PASS', None)
        
    if not adminpass:
        from app import PASSPATH
        with open(PASSPATH) as passfile:
            try: adminpass = passfile.read()
            # super rudimentary for now
            finally: pass
        
    if not adminpass:
        raise ValueError("Admin password definition not found!")
        
    return adminpass
    
    