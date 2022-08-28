# 2022-08-28
# 위장
from collections import defaultdict
from itertools import combinations

def solution(clothes):
    dic = defaultdict(list)
    res = 1
    for item, key in clothes:
        dic[key].append(item)

    print(dic)
    for key in dic.keys():
        res *= len(dic[key]) + 1

    res -= 1
    print(res)
    return res

solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]])