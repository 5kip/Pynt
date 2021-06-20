def find_max_index(lizt, lenleanse = None):
    if lenleanse != 0 :
        index = 0
        if lenleanse == None:
            lenleanse = len(lizt)
        current_biggest_num = lizt[0]
        for i in range(1, lenleanse):
            if current_biggest_num < lizt[i]:
                current_biggest_num = lizt[i]
                index = i
        return index 
    return -1

def sort(lizt):
    lenlease = len(lizt)
    for number in range(0, lenlease):
        maxindex = find_max_index(lizt, lenlease)
        lenlease -= 1
        lizt[maxindex], lizt[lenlease] = lizt[lenlease], lizt[maxindex]
    return lizt

print(sort([1,8,124,1,1231,20000,23412341234,123]))