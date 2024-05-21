#!/usr/bin/python3
'''LIFOCache Caching System'''
from more_itertools import last
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
	'''LIFOCache Caching System'''
	def put(self, key, item):
		'''assigns to the dictionary self.cache_data the item value for the key key'''
		if not key or not item:
			return
		if len(self.cache_data) == BaseCaching.MAX_ITEMS:
			last_key = last(self.cache_data)
			self.cache_data.pop(last_key)
			print(f"DISCARD: {last_key}")
		self.cache_data[key] = item
	
	def get(self, key):
		''' returns the value in self.cache_data linked to key.'''
		if key:
			if key not in self.cache_data.keys():
				return
			return self.cache_data[key]
