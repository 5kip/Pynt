def compare_bigger(long_string, short_string):
    for i in range(0, len(short_string)):
        diff = ord(long_string[i]) - ord(short_string[i])
        if diff != 0:
            return diff

    if len(long_string) == len(short_string):
        return 0
    return 1   
    
def compare(string1, string2):
    if len(string1) < len(string2):
        return -compare_bigger(string2, string1)
    return compare_bigger(string1, string2)