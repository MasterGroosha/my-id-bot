from math import inf
from cachetools import TTLCache

"""
This is a simple TTL Cache, so that my_chat_member doesn't trigger on group to supergroup migration event
"""
cache = TTLCache(maxsize=inf, ttl=10.0)
