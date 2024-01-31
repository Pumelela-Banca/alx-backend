#!/usr/bin/env python3
"""
Has a class called basic cache that stores
basic information
"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
    Inherits from BasicCaching and implements put and get
    """

    def put(self, key, item):
        """
        Put objects into self.cache_data
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """
        Gets key from self.cache_data
        """
        if key not in self.cache_data.keys():
            return None
        return self.cache_data[key]
