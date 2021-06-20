huyist = [0, 2, 4]

def find_num_module(num):
    if num < 0:
        return -num
    return num

def find_av(lizt):
    if len(lizt) != 0:
        curr_num_sum = 0
        for num in lizt:
            curr_num_sum += num
        return curr_num_sum / len(lizt)
    return "bruhh empty listtttttt"

def find_otclo(lizt):
    if len(lizt) != 0:
        average = find_av(lizt)
        otklonist = []
        for num in lizt:
            deviation = average - num
            deviation = find_num_module(deviation)
            otklonist.append(deviation)
        return otklonist
    return "bruhh empty listtttttt"

def OtclAverage(lizt):
    if len(lizt) != 0:
        return "Среднее :", find_av(lizt), "Отклонение :", find_otclo(lizt)
    return "bruhh empty listtttttt"

def test_aver():
    assert(find_av([0, 2, 4]) == 2)
    assert(find_av([-0, -2, -4]) == -2)
    assert(find_av([]) == "bruhh empty listtttttt")

def AtcloTester():
    assert(find_otclo([0, 2, 4]) == [2, 0, 2])
    assert(find_otclo([-0, -2, -4]) == [2, 0, 2])
    assert(find_otclo([]) == "bruhh empty listtttttt")

test_aver()
AtcloTester()

print(OtclAverage(huyist))