import sys

sys.stdin = open("input.txt", "r")
n = int(input())

num_list = [0] * (n + 1)
num_list[0] = (0, 0)
num_set = set()

for index in range(n):
    num = int(input())
    num_list[index] = (index, num)
    num_set.add(num)


while True:
new_list = [(0, 0)]
for i in num_set:
    new_list.append(num_list[i])




