def permute(arr):
    result = [tuple(arr)]
    c = [0] * len(arr)
    i = 0  # start
    while i < len(arr):
        # print(i)
        # print(c)
        # print(result)
        if c[i] < i:
            if i % 2 == 0:
                arr[0], arr[i] = arr[i], arr[0]
            else:
                arr[c[i]], arr[i] = arr[i], arr[c[i]]
            result.append(tuple(arr))
            c[i] += 1
            i = 0
        else:
            c[i] = 0

            i += 1
    return result


# arr = [i for i in range(1, 5)]
arr = list(range(20))
a = permute(arr)
print(len(a))
print(len(set(a)))

import itertools

permutations = itertools.permutations

print(len(list(permutations(arr))))