import time

class Cache:
    def __init__(self, ttl_seconds=5):
        self.ttl = ttl_seconds
        self.data = {}

    def get(self, key):
        entry = self.data.get(key)
        if not entry:
            return None
        value, timestamp = entry
        if time.time() - timestamp > self.ttl:
            return None
        return value

    def set(self, key, value):
        self.data[key] = (value, time.time())
