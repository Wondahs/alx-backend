#!/usr/bin/python3
'''LIFOCache Caching System'''
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    '''LIFOCache Caching System'''
    __d_count = -2
    def put(self, key, item):
        '''assigns to the dictionary self.cache_data the item value for the key key'''
        if not key or not item:
            return
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            keys = list(self.cache_data.keys())
            last_key = keys[LIFOCache.__d_count]
            self.cache_data.pop(last_key)
            print(f"DISCARD: {last_key}")
            LIFOCache.__d_count -= 1
            if LIFOCache.__d_count == -4:
                LIFOCache.__d_count = -2

    def get(self, key):
        ''' returns the value in self.cache_data linked to key.'''
        if key:
            if key not in self.cache_data.keys():
                return
            return self.cache_data[key]
