print('importing module')

test = 'test string'


def find_index(list_to_search, keyword):
    '''returns the element and index in the list given , else returns 1'''
    for ele, strin in enumerate(list_to_search):
        if strin == keyword:
            return '{} {}'.format(ele, strin)

    return -1
