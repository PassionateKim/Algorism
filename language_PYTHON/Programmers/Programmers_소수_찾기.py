# 소수 찾기
# 복습 횟수:4, 00:45:00, 복습필요O
from copy import deepcopy
def dfs(numbers, li : list, cnt, number_list: set):
    # 탈출조건
    if len(li) == cnt:
        tmp = deepcopy(li)
        number_list.add(tuple(tmp))
        return

    for i in range(len(numbers)):
        if visited[i] == 1: continue

        li.append(numbers[i])
        visited[i] = 1 # 방문처리
        dfs(numbers, li, cnt, number_list)
        li.pop()
        visited[i] = 0 # 원상 복구

    return

def isPrime(val):
    if val < 2:
        return False
    
    for i in range(2, val):
        if val % i == 0:
            return False
    
    return True


def solution(numbers):
    global visited
    
    number_list = set()
    numbers = list(map(str, numbers))

    for i in range(1, len(numbers)+1):
        visited = [0 for _ in range(len(numbers))]
        dfs(numbers, [], i,  number_list)
    
    # 구하기
    result = set()
    for number in number_list:
        number = int("".join(number))
        
        
        if isPrime(number):
            result.add(number)
    
    return len(result)

print(solution("17"))