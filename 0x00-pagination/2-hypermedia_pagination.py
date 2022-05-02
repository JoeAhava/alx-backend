#!/usr/bin/env python3
'''
simple helper function returning
'''


import csv
import math
from pydoc import pager
from typing import List


def index_range(page, page_size):
    '''
    returns range of index of pagination
    '''
    return ((page - 1) * page_size, ((page - 1) * page_size) + page_size)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        '''
        returns the exact value requested
        '''
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        data = self.dataset()
        tpl = index_range(page=page, page_size=page_size)
        if len(data) < tpl[0] or len(data) < (tpl[0] + tpl[1]):
            return []
        return data[tpl[0]: tpl[1]]

    def next(self, page=1, page_size=1):
        '''
        returns next page or None
        '''
        tpl = index_range(page=page + 1, page_size=page_size)
        data = self.dataset()
        try:
            next_data = data[tpl[0]: tpl[1]]
            if len(next_data) > 0:
                return page + 1
            else:
                return None
        except IndexError:
            return None

    def prev(self, page=1, page_size=1):
        '''
        returns prev page or None
        '''
        tpl = index_range(page=page - 2, page_size=page_size)
        data = self.dataset()
        try:
            next_data = data[tpl[0]: tpl[1]]
            if len(next_data) > 0:
                return page - 1
            else:
                return None
        except IndexError:
            return None

    def get_hyper(self, page: int = 1, page_size: int = 10) -> List[List]:
        '''
        returns the hyper info for page value requested
        '''
        data = self.get_page(page=page, page_size=page_size)
        return {
            'page_size': len(data),
            'page': page,
            'data': data,
            'next_page':  self.next(page=page),
            'prev_page': self.prev(page=page),
            'total_pages': len(self.dataset()),
        }
