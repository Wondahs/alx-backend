#!/usr/bin/python3
'''LFUCache Caching System'''
from base_caching import BaseCaching
import time


class LFUCache(BaseCaching):
    '''LFUCache Caching System'''
    __d_count = {}
    __d_time = {}
    def put(self, key, item):
        '''assigns to the dictionary self.cache_data the item value for the key key'''
        if not key or not item:
            return
        self.cache_data[key] = item
        LFUCache.__d_count[key] = 0
        LFUCache.__d_time[key] = time.time()
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            min_val = min(list(LFUCache.__d_count.values()))
            min_list = []
            minkey = None
            for k, v in LFUCache.__d_count.items():
                if k is not key and v == min_val:
                    minkey = k
                    min_list.append(k)
            if len(min_list) > 0:
                now = time.time()
                diff = 0
                for k, v in LFUCache.__d_time.items():
                    t_diff = now - v
                    if k is not key and t_diff > diff:
                        minkey = k
                        diff = t_diff

            del self.cache_data[minkey]
            del LFUCache.__d_count[minkey]
            del LFUCache.__d_time[minkey]
            print(f"DISCARD: {minkey}")

    def get(self, key):
        ''' returns the value in self.cache_data linked to key.'''
        if key:
            if key not in self.cache_data.keys():
                return
            LFUCache.__d_count[key] += 1
            LFUCache.__d_time[key] = time.time()
            return self.cache_data[key]
