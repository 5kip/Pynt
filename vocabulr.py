string ="aakqaor"

def create_alphabet_range(first_letter = "a", last_letter = "z", amount = 1):
    if ord(last_letter) < ord(first_letter) :
        last_letter, first_letter = first_letter, last_letter
    if ord(first_letter) < ord("a"):
        first_letter = "a"
    if ord(last_letter) > ord("z"):
        last_letter = "z"
    alphabet = []
    for i in range(ord(first_letter), ord(last_letter) + 1):
        el = (chr(i) * amount)
        alphabet += el
    return "".join(alphabet)

def findamount(lizt, thing):
    amount = 0
    for el in lizt:
        if el == thing:
            amount += 1
    return amount

def letter_amount_dict(string):
    counter = {}
    for el in string:
        if not el in counter:
            counter[el] = 1
        else:
            counter[el] += 1
    return counter

print(create_alphabet_range("1", "1"))
print(letter_amount_dict(string))