list_box = list(map(int,input().split()))

ans = 0
for i in range(len(list_box)):
    tall = list_box[i]
    count = len(list_box) - 1 - i
    for block in list_box[i+1:]:
        if tall <= block:
            count -= 1
    if count >= ans:
        ans = count

print(ans)