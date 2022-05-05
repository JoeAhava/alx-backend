#!/usr/bin/env python3
'''
basic caching
'''


from requests import delete
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    '''
    Class implementing a fifo cache
    '''

    def __init__(self):
        '''
        initialize basecache
        '''
        super().__init__()

    def put(self, key, item):
        '''
        puts item in the cache
        '''
        if key and item:
            if key in self.cache_data.keys():
                self.cache_data[key] = item
            elif len(self.cache_data.keys()) < self.MAX_ITEMS:
                self.cache_data[key] = item
            else:
                self.cache_data[key] = item
                print(f"DISCARD: {list(self.cache_data.keys())[0]}")
                self.cache_data.pop(list(self.cache_data.keys())[0])

    def get(self, key):
        '''
        get item from cache
        '''
        return self.cache_data.get(key, None)
