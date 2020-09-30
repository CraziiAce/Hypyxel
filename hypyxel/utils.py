"""
© 2020 CraziiAce
"""

import requests

from hypyxel.errors import UUIDNotFoundError, ApiKeyError

class Utils:
    """A base class for utility functions"""

    
    def __init__(self, api_key):
        self.key = api_key

    def _get_uuid(self, username):
        try:
            return requests.request("GET", f"https://playerdb.co/api/player/minecraft/{username}").json()['data']['player']['raw_id']
        except:
            raise UUIDNotFoundError(f"A UUID could not be found for {username}")
            
    def _key_check(self):
        """An internal function to check if the key exists"""
        if not key:
            raise ApiKeyError("You need to set the key with set_api_key()")

    def _get_key(self):
        return self.key[0]
