# 2022-08-09
# 2022-08-10
# 2022-08-13
# 소수 찾기
from itertools import permutations


def solution(numbers):
    def isPrime(val : int):
        if val < 2:
            return False

        # 나눠지면 소수가 아니다.
        for i in range(2, val):
            if val % i == 0:
                return False

        return True
    answer = set()    
    for i in range(1, len(numbers) + 1):
        per = list(permutations(numbers, i))
        tmp = set()
        # 중복 제거하기
        for i in per:
            tmp.add(i)
        # 가능한 값 다 넣기
        for tu in tmp:
            string = ""
            for j in range(len(tu)):
                if j == 0 and tu[j] == '0': continue
                string += tu[j]
            
            if string and isPrime(int(string)):
                answer.add(int(string))
    

    return len(answer)

print(solution("17"))