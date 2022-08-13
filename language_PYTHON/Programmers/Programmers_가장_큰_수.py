# 2022-08-13
# 가장 큰 수
from itertools import permutations

def solution(numbers):
    answer = ''
    num_list = []
    # 1. num을 str로 저장
    for num in numbers:
        num_list.append(str(num))

    num_list.sort(key=lambda x : x*3, reverse=True)
    
    answer = str(int("".join(num_list)))
    a = ["30","3"]
    a.sort()
    print(a)
    return answer

print(solution([221, 2]))