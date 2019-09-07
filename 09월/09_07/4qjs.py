aa = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
bb = ["fro??", "????o", "fr???", "fro???", "pro?"]


def solution(words, queries):
    new_words = dict()
    for word in words:
        if new_words.get(len(word)):
            new_words[len(word)].add(word)
        else:
            new_words[len(word)] = set()
            new_words[len(word)].add(word)

    ans = []
    for checker in queries:
        min_ans = 0
        if new_words.get(len(checker)):
            check_list = new_words[len(checker)]
        else:
            ans.append(min_ans)
            continue

        p = checker.count('?')
        cc = 0
        if p:
            if checker[0] == '?':
                cc = 1
            else:
                cc = 2

        if cc == 0:
            cnt = check_list.count(checker)
        elif p == len(checker):
            cnt = len(check_list)
        else:
            cnt = 0
            for word in check_list:
                if cc == 1:
                    if word[p:] == checker[p:]:
                        cnt += 1
                elif cc == 2:
                    if word[:-p] == checker[:-p]:
                        cnt += 1

        ans.append(cnt)
    answer = ans
    return answer

print(solution(aa,bb))