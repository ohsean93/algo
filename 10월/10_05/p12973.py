def solution(s):
    ans = [s[0]]
    n = len(s)
    i = 1
    while n != i:
        if ans and ans[-1] == s[i]:
            ans.pop()
        else:
            ans.append(s[i])
        i += 1
    if len(ans):
        return 0
    return 1