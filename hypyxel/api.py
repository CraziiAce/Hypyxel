import requests

from hypyxel.errors import AdvApiKeyError, ApiKeyError
from hypyxel.utils import _get_uuid

hypixel_base_url = "https://api.hypixel.net"

class HypixelAPI:
    """Class for interacting with the Hypixel API"""
    def __init__(self, api_key):
        self.key = api_key
        self.endpoints = {
            "status":"/status", 
            "watchdog":"/watchdogstats", 
            "player":"/player",
            "leaderboards":"/leaderboards",
            "key":"/key",
            "game_counts":"/gameCounts"
        }
        self.hypixel_base_url = "https://api.hypixel.net"

    def _key_check(self):
        if not self.key:
            raise ApiKeyError

    def adv_key_check(self):
        """Check if a key is valid."""
        r = requests.request("GET", f"{hypixel_base_url}{self.endpoints['key']}?key={self.key}").json()
        if not r["success"]:
            raise AdvApiKeyError("That api key didn't work...")
        else:
            return True

    def get_endpoints(self):
        """Returns a dict of functions and the associated endpoint"""
        return self.endpoints

    def status(self, username):
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

        self._key_check()
        return requests.request("GET", f"{self.hypixel_base_url}{self.endpoints['status']}?key={self.key()}?uuid={_get_uuid(username)}").json()

    def watchdog(self):
        """Get watchdog stats
        example response:
        .. container:: operations

            .. describe:: len(x)

                {"success":true,"watchdog_lastMinute":1,"staff_rollingDaily":2011,"watchdog_total":5501269,"watchdog_rollingDaily":2786,"staff_total":1823141}
        Raises: `ApiKeyError` if the api key has not been set.
        """
        self._key_check()
        return requests.request("GET", f"{self.hypixel_base_url}{self.endpoints['watchdog']}?key={self.key()}").json()

    def player(self, username):
        """Get information for a player\n
        Important: `username` MUST be a username, not a UUID.
        This is not the same as `status`
        The example response is too big to put here
        Raises: `ApiKeyError` if the api key has not been set, or `UUIDNotFoundError` if a uuid could not be found for the username.
        """
        self._key_check()
        return requests.request("GET", f"{self.hypixel_base_url}{self.endpoints['player']}?key={self.key()}?uuid={_get_uuid(username)}").json()
    def leaderboards(self):
        """Get game leaderboards
        The example response is too big to put here.
        Raises: `ApiKeyError` if the api key has not been set.
        """
        return requests.request("GET", f"{self.hypixel_base_url}{self.endpoints['leaderboards']}?key={self.key}").json()
    def game_counts(self):
        """Get player counts for different game modes.
        The example response is too big to put here.
        Raises: `ApiKeyError` if the api key has not been set.
        """
        return requests.request("GET", f"{self.hypixel_base_url}{self.endpoints['game_counts']}?key={self.key}")
