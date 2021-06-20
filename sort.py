import string_compare as str_compare

def default_is_grater(a, b):
    return a > b
def is_smaller(a, b):
    return b > a

def findex(lizt, el_to_find):
    for i in range(0, len(lizt)):
        if lizt[i] == el_to_find:
            return i
    return -1

def str_compare_adapter(str1, str2, compare_method = default_is_grater):
    if compare_method == default_is_grater:
        return str_compare.compare(str1, str2) > 0
    return str_compare.compare(str1, str2) < 0

def find_max_index(lizt, last_index = None, compare_method = default_is_grater):
    if len(lizt) == 0:
        return -1
    if last_index == None:
        last_index = len(lizt)
    index = 0
    if isinstance(lizt[0], str):
        currentmaxstr = lizt[0]
        for i in range(1, last_index):
            if str_compare_adapter(lizt[i], currentmaxstr, compare_method):
                currentmaxstr = lizt[i]
                index = i
    else:
        currentmaxnum = lizt[0]
        for i in range(1, last_index):
            if compare_method(lizt[i], currentmaxnum):
                currentmaxnum = lizt[i]
                index = i
    return index

def find_max_index_test():
    assert(find_max_index([])  == -1)
    assert(find_max_index([1]) == 0 )
    assert(find_max_index([1, 8, -24]) == 1)
    assert(find_max_index([1, 8, -14], 3, is_smaller) == 2 )

def sort(lizt, compare_method = default_is_grater):
    lenlizt = len(lizt)
    for number in range(0, lenlizt):
        max_num_index = find_max_index(lizt, lenlizt, compare_method)
        lenlizt -= 1
        lizt[max_num_index], lizt[lenlizt] = lizt[lenlizt], lizt[max_num_index]
    return lizt

def sort_test():
    assert(sort([]) == []  )
    assert(sort([2]) == [2])
    assert(sort([1, 8, -14]) == [-14, 1, 8])
    assert(sort([1, 8, -14], is_smaller) == [8, 1, -14] )
    assert(sort(["abc", "bcd"]) == ["abc", "bcd"])
    assert(sort(["abc", "bcd"], is_smaller) == ["bcd", "abc"])

find_max_index_test()
sort_test()