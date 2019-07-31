import csv
from random import shuffle

with open('student.csv', mode = 'r', encoding='utf8', newline= '') as f:
    csv_reader = csv.reader(f)
    dict_ssafy21 = {}

    for row in csv_reader:
        student_id = int(row[0])
        name = row[1]
        dict_ssafy21[student_id]=name

sheet = list(range(1,27))
shuffle(sheet)


for i in range(5):
    aa = sheet[:6]
    for student_id in aa:
        print(dict_ssafy21.get(student_id), end=" ")
    sheet = sheet[6:]
    print()

