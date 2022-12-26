# N과 M (1)
import sys
si = sys.stdin.readline
N, M = map(int, si().split())
visited = [0 for i in range(N+1)]
answer = []


def dfs(cnt):
    
    if cnt == M:
        print(*answer)
        return

    for val in range(1, N+1):
        if visited[val] == 0: # 방문하지 않은 경우만
            answer.append(val)
            visited[val] = 1 # 방문처리
            dfs(cnt + 1)

            answer.pop() # 초기화
            visited[val] = 0 # 초기화
    
    return

dfs(0)