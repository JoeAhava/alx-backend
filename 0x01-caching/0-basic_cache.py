#!/usr/bin/env python3
'''
basic caching
'''


from base_caching import BaseCaching


class BasicCache(BaseCaching):
    '''
    Class implementing a basic cache
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
        self.cache_data[key] = item

    def get(self, key):
        '''
        get item from cache
        '''
        result = None
        if key is None:
            return result
        try:
            result = self.cache_data[key]
        except KeyError:
            result = None
        return result
