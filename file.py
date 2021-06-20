import sort

class Student:
    def __init__(self, name, klas, average_grade):
        self.name = name
        self.klas = klas
        self.average_grade = average_grade

vosmoy_v = [
    Student("Feodosiy", "2", 3.8),
    Student("Feodosia", "2", 1.2),
    Student("Vova", "4", 4.3)    ,
    Student("Peta", "8", 12 )    ,
    Student("Faa", "9", 11.5)    ,
    Student("AleXDnder", "14", 3)]

def sort_av_grade(srudent1, srudent2):
    return srudent1.average_grade > srudent2.average_grade

sort.sort(vosmoy_v, sort_av_grade)
for srudent in vosmoy_v:
    print(srudent.average_grade)