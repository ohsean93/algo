a = int('0x196EBC5A316C578', 16)

print(a)

while a % 2 - 1:
    a //= 2
print(a)

len_code = []
for r in range(1, 500//56+1):
    len_code.append(2**(r * 56))
print(len_code)
d = 1
for i in range(500//56+1):
    if a < len_code[i]:
        d = i + 1
        break
print(d)
d = 1
a //= d

print(a)


num_list = {
    13: 0,
    25: 1,
    19: 2,
    61: 3,
    35: 4,
    49: 5,
    47: 6,
    59: 7,
    55: 8,
    11: 9,
}


checker = a
code = []
while checker:
    code.append(num_list[checker % 128])
    checker //= 128
a, b = sum(code[0::2]), sum(code[1::2])
if (a+3*b) % 10:
    ans = 0
else:
    ans = a + b
print(ans)