# 2022-08-11
from collections import deque
def solution(maps):
    answer = 0
    n = len(maps)
    m = len(maps[0])
    visited = [[0 for _ in range(m)] for _ in range(n)]
    dir = [(-1,0), (1,0), (0,-1), (0,1)]

    def bfs(x, y, cnt):
        # q 초기화
        q = deque()
        q.append([x, y, cnt + 1])
        visited[x][y] = 1 # 방문처리
        
        while q:
            x, y, cnt = q.popleft()
            # 탈출조건
            if x == n-1 and y == m-1:
                return cnt 

            for i in range(4):
                nx, ny = x + dir[i][0], y + dir[i][1]
                if not (0<=nx<n and 0<=ny<m): continue

                if visited[nx][ny] == 0 and maps[nx][ny] == 1:
                    visited[nx][ny] = 1 # 방문처리
                    q.append([nx, ny ,cnt + 1])

        return -1
    
    answer = bfs(0,0,0)
    return answer

print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))