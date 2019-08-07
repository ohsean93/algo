from random import shuffle
a = list(range(1,26))
shuffle(a)

matrix = [[]]*7
for line_num in range(1,6):
    line = [a[0]] + a[:5] +[a[4]]
    matrix[line_num] = line.copy()
    a = a[5:]

matrix[0] = matrix[1].copy()
matrix[6] = matrix[5].copy()

print(matrix)

vactor = [(1,0),(0,1),(-1,0),(0,-1)]
all_sum = 0

for x in range(1,6):
    for y in range(1,6):
        sum_num = 0
        num1 = matrix[x][y]
        for mod in range(4):
            x_dal, y_dal = vactor[mod]
            num2 = matrix[x+x_dal][y+y_dal]
            num = num1 - num2
            if num < 0:
                sum_num += -num
            else:
                sum_num += num

        all_sum += sum_num

print(all_sum)
