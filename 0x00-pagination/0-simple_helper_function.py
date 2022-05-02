#!/usr/bin/env python3
'''
simple helper function returning
'''


def index_range(page, page_size):
    '''
    returns range of index of pagination
    '''
    return ((page - 1) * page_size, ((page - 1) * page_size) + page_size)


if __name__ == '__main__':
    res = index_range(1, 7)
    print(type(res))
    print(res)

    res = index_range(page=3, page_size=15)
    print(type(res))
    print(res)
