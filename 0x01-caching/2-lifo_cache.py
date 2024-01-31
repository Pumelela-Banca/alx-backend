#!/usr/bin/env python3
"""
Implementation of LIFO
"""
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """
    class with lifo caching
    """
    def __init__(self):
        """
        added order of items
        """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """
        Puts items into self.cache_data
        """
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.cache_data[key] = item
            return
        if len(self.order) >= BaseCaching.MAX_ITEMS:
            print("DISCARD:", self.order[-1])
            del self.cache_data[self.order[-1]]
            self.order = self.order[:-1].copy()
        self.order.append(key)
        self.cache_data[key] = item

    def get(self, key):
        """
        Get key
        """
        if key is None:
            return None
        return self.cache_data[key]
