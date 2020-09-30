"""
© 2020 CraziiAce
This code may be used freely as long as long it bears this copyright statement at the start.
"""

class ApiKeyError(Exception):
    """The Hypixel API key is invalid/hasn\'t been set. Set it with `set_api_key()`"""
    pass

class UUIDNotFoundError(Exception):
    """A UUID could not be found for the passed user name"""
    pass
