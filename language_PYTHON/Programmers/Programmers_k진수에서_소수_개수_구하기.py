# 복습 횟수:0, 01:00:00, 복습필요O
from collections import deque
import math
def check(val):
    if(val == 1):
        return False
    
    for i in range(2, int(math.sqrt(val)) + 1 ):
        if(val % i == 0):
            return False
    
    return True

def solution(n, k):
    answer = 0

    convertered = deque()

    while(n != 0):
        convertered.appendleft(str(n % k))
        n = n // k
    
    isPrime = list()
    start = 0
    end = 0
    for i in range(len(convertered)):
        if convertered[i] != '0':
            end += 1
            if end == len(convertered): # 마지막이라면
                isPrime.append(list(convertered)[start:end])
        else: # 0 이라면
            if(start == end): 
                start = i + 1
                end = i + 1
                continue

            isPrime.append(list(convertered)[start:end])
            start = i+1
            end = i+1

    candidate = []
    for prime in isPrime:
        prime = int(''.join(prime))
        candidate.append(prime)
    
    for c in candidate:
        if(check(c)):
            answer += 1

    return answer

print(solution(110011, 10))