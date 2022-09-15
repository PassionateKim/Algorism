# 2022-09-15
# 2022-09-16
# 모음사전

from itertools import product

def solution(word):
    answer = []
    for i in range(1, 6):
        tmp = product(['A', 'E', 'I', 'O', 'U'], repeat = i)
        for i in tmp:
            answer.append("".join(i))

    answer.sort()

    return answer.index(word) + 1    

print(solution("AAAAE"))