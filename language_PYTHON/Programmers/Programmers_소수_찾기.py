# 소수 찾기
# 복습 횟수:5, 00:45:00, 복습필요X

import math
from itertools import permutations
def isPrime(input):
    if input == 0 or input == 1:
        return False
        
    if input == 2:
        return True
    
    for i in range(2, int(math.sqrt(input)) + 1):
        if input % i == 0:
            return False

    return True

def solution(number_string):
    answer = set()

    for i in range(1, len(number_string) + 1):
        permutation_list = list(permutations(range(len(number_string)), i))
        
        for case in permutation_list:
            tmp = ""
            for index in case:
                tmp = tmp + number_string[index]
            

            tmp_int = int(tmp)

            if isPrime(tmp_int):
                answer.add(tmp_int)

    return len(answer)


solution("17")