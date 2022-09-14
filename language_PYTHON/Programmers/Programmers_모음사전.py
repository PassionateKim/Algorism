# 2022-09-15
# 모음사전
from itertools import product

def solution(word):
    answer = 0
    words = []
    for i in range(1, 6):
        for c in product(['A', 'E', 'I', 'O', 'U'], repeat=i):
            words.append(''.join(list(c)))
    print(words)
    return answer

solution("AAAAE")