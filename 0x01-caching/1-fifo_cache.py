#!/usr/bin/python3
'''FIFOCache Caching System'''
from more_itertools import first
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
	'''FIFOCache Caching System'''
	def put(self, key, item):
		'''assigns to the dictionary self.cache_data the item value for the key key'''
		if not key or not item:
			return
		self.cache_data[key] = item
		if len(self.cache_data) > BaseCaching.MAX_ITEMS:
			first_key = first(self.cache_data)
			self.cache_data.pop(first_key)
			print(f"DISCARD: {first_key}")
	
	def get(self, key):
		''' returns the value in self.cache_data linked to key.'''
		if key:
			if key not in self.cache_data.keys():
				return
			return self.cache_data[key]
