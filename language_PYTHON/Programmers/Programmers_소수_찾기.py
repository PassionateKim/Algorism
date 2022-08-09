# 2022-08-09
# 소수 찾기
from itertools import combinations, permutations
from collections import deque;

def solution(numbers):
    def checkPrime(num):
        # 예외 조건
        if num == 1:
            return False

        for i in range(2, num//2 + 1):
            # 나눠지면
            if num % i == 0:
                return False

        return True
    numbers = list(map(str, numbers))
    answer = 0
    check = set()
    for i in range(1, len(numbers) + 1):
        combi = set(combinations(numbers, i))
        # combi [('1', '7')]
        combi = list(combi)
        for i in combi:
            # permu {('1','7'), ('7','1')}
            permu = set(permutations(i))

            # print("===")
            # print("permu",permu)
            for p in permu:
                p = deque(p)
                # 11과 011은 같은 숫자로 취급합니다.
                while p and p[0] == '0':
                    p.popleft()
                
                # p를 int 타입으로 변환하고 소수인지 확인하기
                if p:
                    
                    p = int("".join(p))
                    
                    # primeNum이면
                    if p not in check and checkPrime(p):
                        answer += 1
                        check.add(p)

                
    return answer

print(solution("17"))