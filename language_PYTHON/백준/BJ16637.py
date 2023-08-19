# 괄호 추가하기
# 복습 횟수:1, 02:00:00, 복습필요3
import sys
from collections import deque
si = sys.stdin.readline 
N = int(si())
arr = list(map(str, si().rstrip()))

answer = -sys.maxsize
visited = [0 for i in range(N)]
max_depth = ((N // 2) + 1) // 2

def calculate(first, second, arr):
    operator = arr[first + 1]
    first = int(arr[first])
    second = int(arr[second])

    if operator == '+':
        return str(first + second)
    
    elif operator == '*':
        return str(first * second)

    else:
        return str(first - second)
    
def dfs(depth, current):
    global answer
    
    if (depth == max_depth):
        
        # 계산하기
        if 1 in visited: # 괄호가 하나라도 있는 경우
            tmp = []
            isgwalho = False
            for i in range(N):
                if visited[i] == 1: # 괄호가 시작하면
                    if not isgwalho:
                        isgwalho = True
                    else: # 괄호가 끝나면
                        tmp_result = calculate(i-2, i, arr)
                        tmp.append(tmp_result)
                        isgwalho = False # 괄호 초기화
                else: # 괄호가 아니라면
                    if not isgwalho:
                        tmp.append(arr[i])


            candidate_result = calculateList(tmp)     
            answer = max(answer, candidate_result)


        else: #괄호가 하나도 없는 경우
            candidate_result = calculateList(arr)     
            answer = max(answer, candidate_result)
        
        
        return
    
    dfs(depth + 1, current)

    for idx in range(current, N-1):
        if visited[idx] != 0: continue 
        if idx % 2 == 1: continue
        visited[idx] = 1 # 방문처리
        visited[idx + 2] = 1 # 방문처리
        dfs(depth + 1, idx + 1)

        visited[idx] = 0 # 초기화
        visited[idx + 2] = 0 

def calculateList(tmp):
    q = deque()
    for i in range(len(tmp)):
        if tmp[i] not in ['+', '-','*']:
            q.append(int(tmp[i]))

        if len(q) == 2:
            first = q.popleft()
            second = q.popleft()

            operator = tmp[i-1]
            if operator == '+':
                result_val = first + second
            elif operator == '*':
                result_val = first * second
            else:
                result_val = first - second

            q.append(result_val)# 초기화
        
    result = q.popleft()

    return result

dfs(0, 0)
print(answer)