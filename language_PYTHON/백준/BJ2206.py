# 2022-04-29
# 2022-05-29
# 2022-08-29
# 벽 부수고 이동하기
import sys
from collections import deque
si = sys.stdin.readline
N, M = map(int, si().split())
graph = []
answer = 0
# 초기화
for i in range(N):
    graph.append(list(map(int, si().strip())))

# 3차원으로 visited를 구분해주어야한다.
visited = [[[0,0] for _ in range(M)] for _ in range(N)]
# 상하좌우
dir = [(-1,0), (1,0), (0,-1), (0,1)]
def bfs(x, y, cnt, possible):
    q = deque()
    q.append([x, y, cnt, possible])
    # 1은 한번 깰 수 있는 상태
    visited[x][y][possible] = 1 # 방문처리
    while q:
        x, y, cnt, possible = q.popleft()
        # 탈출조건
        if x == N-1 and y == M-1:
            return cnt

        # dir 탐색
        for idx in range(4):
            nx, ny = x + dir[idx][0], y + dir[idx][1]
            # 예외처리
            if not (0<=nx<N and 0<=ny<M): continue
            if visited[nx][ny][possible] == 1: continue
            
            # 벽인 경우
            if graph[nx][ny] == 1:
                if possible == 1: 
                    q.append([nx, ny, cnt+1, 0])
                    visited[nx][ny][possible] = 1 #방문처리

            # 벽이 아닌 경우
            else:
                q.append([nx, ny, cnt+1, possible])
                visited[nx][ny][possible] = 1 #방문처리
    # 가능하지 않은 경우
    return -1

answer = bfs(0, 0, 1, 1)
print(answer)