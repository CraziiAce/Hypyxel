import requests

from hypyxel.errors import UUIDNotFoundError, ApiKeyError

key = ""

def _get_uuid(username):
    try:
        return requests.request("GET", f"https://playerdb.co/api/player/minecraft/{username}")['data']['player']['raw_id']
    except:
        raise UUIDNotFoundError(f"A UUID could not be found for {username}")

def set_api_key(user_key):
    """Set the API key"""
    global key
    key = user_key

def _key_check():
    """An internal function to check if the key exists"""
    if not key:
        raise ApiKeyError("You need to set the key with set_api_key()")

def _get_key():
    global key
    return key
