#!/usr/bin/env python3
"""
Class for MRU cache
"""
BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """
    Class for MRU cache
    """
    def __init__(self):
        """
        initialisation
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
        gets item and saves most recently used item
        """
        if key is None:
            return None
        if key not in self.cache_data:
            return None
        if self.order:
            new = [x for x in self.order if x != key]
            self.order = new + [key]
        return self.cache_data[key]
