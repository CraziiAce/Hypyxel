import requests

class ApiKeyError(Exception):
    """The Hypixel API key is invalid/hasn\'t been set. Set it with `set_api_key()`"""
    pass

class UUIDNotFoundError(Exception):
    """A UUID could not be found for the passed user name"""
    pass


key = ""
hypixel_base_url = "https://api.hypixel.net"
endpoints = {"status":"/status", "watchdog":"/watchdogstats", "player":"/player"}

def _get_uuid(username):
    try:
        return requests.request("GET", f"https://playerdb.co/api/player/minecraft/{username}")['player']['meta']['raw_id']
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

def get_endpoints():
    """Returns a dict of fuctions and the associated endpoint"""
    return endpoints

def status(username):
    """Get the status for a player\n
    Important: `username` MUST be a username, not a UUID.
    This is not the same as `player`
    example response content if online:     
    .. container:: operations

        .. describe:: len(x)

            {"success":true,"session":{"online":true,"gameType":"SKYBLOCK","mode":"hub"}}
    
    or if not online:
    
    .. container:: operations

        .. describe:: len(x)
            {"success":true,"session":{"online":false}}
    Raises: `ApiKeyError` if the api key has not been set, or `UUIDNotFoundError` if a uuid could not be found for the username.
    """

    _key_check()
    return requests.request("GET", f"{hypixel_base_url}{endpoints['status']}?key={key}?uuid={_get_uuid(username)}")
    
def watchdog():
    """Get watchdog stats
    example response:     
    .. container:: operations

        .. describe:: len(x)

            {"success":true,"watchdog_lastMinute":1,"staff_rollingDaily":2011,"watchdog_total":5501269,"watchdog_rollingDaily":2786,"staff_total":1823141}
    Raises: `ApiKeyError` if the api key has not been set.
    """
    _key_check()
    return requests.request("GET", f"{hypixel_base_url}{endpoints['watchdog']}?key={key}")

def player(username):
    """Get information for a player\n
    Important: `username` MUST be a username, not a UUID.
    This is not the same as `status`
    The example response is too big to put here
    Raises: `ApiKeyError` if the api key has not been set, or `UUIDNotFoundError` if a uuid could not be found for the username.
    """
    _key_check()
    return requests.request("GET", f"{hypixel_base_url}{endpoints['player']}?key={key}?uuid={_get_uuid(username)}")
