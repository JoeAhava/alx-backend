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
        if key is None or item is None:
            return
        if self.cache_data.get(key, None) is not None:
            self.cache_data[key] = item
            return
        if len(self.cache_data) >= self.MAX_ITEMS:
            print('DISCARD: ', list(self.cache_data.keys())[0])
            del self.cache_data[list(self.cache_data.keys())[0]]

        self.cache_data[key] = item

    def get(self, key):
        result = None
        if key is None:
            return result
        try:
            result = self.cache_data[key]
        except KeyError:
            result = None
        return result
