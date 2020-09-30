import requests

from hypyxel.errors import UUIDNotFoundError, ApiKeyError
from hypyxel.utils.utils import _get_key, _get_uuid, _key_check

hypixel_base_url = "https://api.hypixel.net"
endpoints = {
    "status":"/status", 
     "watchdog":"/watchdogstats", 
     "player":"/player"
}

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
    return requests.request("GET", f"{hypixel_base_url}{endpoints['status']}?key={_get_key()}?uuid={_get_uuid(username)}").json()
    
def watchdog():
    """Get watchdog stats
    example response:     
    .. container:: operations

        .. describe:: len(x)

            {"success":true,"watchdog_lastMinute":1,"staff_rollingDaily":2011,"watchdog_total":5501269,"watchdog_rollingDaily":2786,"staff_total":1823141}
    Raises: `ApiKeyError` if the api key has not been set.
    """
    _key_check()
    return requests.request("GET", f"{hypixel_base_url}{endpoints['watchdog']}?key={_get_key()}").json()

def player(username):
    """Get information for a player\n
    Important: `username` MUST be a username, not a UUID.
    This is not the same as `status`
    The example response is too big to put here
    Raises: `ApiKeyError` if the api key has not been set, or `UUIDNotFoundError` if a uuid could not be found for the username.
    """
    _key_check()
    return requests.request("GET", f"{hypixel_base_url}{endpoints['player']}?key={_get_key()}?uuid={_get_uuid(username)}").json()
