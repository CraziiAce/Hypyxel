"""
© 2020 CraziiAce
"""

from hypyxel.errors import UUIDNotFoundError, ApiKeyError

def _get_uuid(self, username):
    try:
        return requests.request("GET", f"https://playerdb.co/api/player/minecraft/{username}").json()['data']['player']['raw_id']
    except:
        raise UUIDNotFoundError(f"A UUID could not be found for {username}")
