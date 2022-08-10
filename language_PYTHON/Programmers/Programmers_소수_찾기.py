# 2022-08-09
# 2022-08-10
# 소수 찾기
from itertools import combinations, permutations
from collections import deque;

def solution(numbers):
    def checkPrime(num):
        # 예외 조건
        if num < 2:
            return False

        for i in range(2, num//2 + 1):
            # 나눠지면
            if num % i == 0:
                return False

        return True

    answer = 0
    numbers = list(numbers)
    tmp = []

    for i in range(1, len(numbers) + 1):
        tmp += list(permutations(numbers, i))
    num =set(int(''.join(t)) for t in tmp)

    for i in num:
        if checkPrime(i):
            answer += 1
    
    return answer

print(solution("17"))