#!/usr/bin/env python3
"""
FIFO caching implementations of put and get
"""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """
    Adds fifo style to BaseCaching
    """
    def __init__(self):
        """
        added order of items
        """
        super().__init__
        self.order = []

    def put(self, key, item):
        """
        Puts items into self.cache_data
        """
        if key is None or item is None:
            return
        if len(self.order) == BaseCaching.MAX_ITEMS:
            print("DISCARD:", self.order[0])
            del self.cache_data[self.order[0]]
            self.order.pop(1)
            self.order += [key]
        self.cache_data[key] = item

    def get(self, key):
        """
        Get key
        """
        if key is None:
            return
        return self.cache_data[key]
