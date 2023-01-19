# 줄어드는 수
# 복습 횟수:0, 00:45:00
import sys
sys.setrecursionlimit(10**6)
si = sys.stdin.readline

N = int(si())
answer = 0
def dfs(count, idx, number : list):
    # 조건을 만족하는 dfs가 존재한다면
    if count == idx:
        global answer 
        answer += 1
        # 만약 원하는 조건을 만족하는 경우라면 exit()
        if (answer == N): 
            print(int("".join(number)))
            exit()

        return
    
    # 백트래킹 - 숫자는 0 ~ 9
    # 숫자는 전의 것보다 작아야함
    for i in range(10):
        # 처음인 경우는 다 통과
        if len(number) == 0:
            number.append(str(i))
            dfs(count, idx+1, number)
            number.pop() # 원상복구
        # 끝보다 i가 작은 경우에만 dfs
        elif int(number[-1]) > i:
            number.append(str(i)) 
            dfs(count, idx+1, number)
            number.pop() # 원상복구

    return

# 최소가 1자리 최대가 10자리 이므로 
for i in range(1, 11):
    dfs(i, 0, [])
    
if N > answer:
    print(-1)