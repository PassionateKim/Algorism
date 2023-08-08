# 꽃길
# 복습 횟수:1, 01:00:00, 복습필요O
import sys
si = sys.stdin.readline 
N = int(si())
graph = []
for i in range(N):
    tmp = list(map(int, si().split()))
    graph.append(tmp)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

answer = sys.maxsize
# 가능한 순서쌍
case_list = list()


for x1 in range(1, N - 1):
    for y1 in range(1, N - 1):
        visited = [[0 for i in range(N)] for i in range(N)]
         
        visited[x1][y1] = 1 # 방문 처리
        for idx in range(4):
            nx, ny = x1 + dx[idx], y1 + dy[idx]
            visited[nx][ny] = 1 # 방문처리
                    
        for x2 in range(1, N - 1):
            for y2 in range(1, N - 1):
                q = list()
                q.append([x2, y2])

                for idx in range(4):
                    nx, ny = x2 + dx[idx], y2 + dy[idx]
                    q.append([nx, ny])

                flag = False
                for x, y in q:
                    if visited[x][y] == 1:
                        flag = True
                
                if flag: continue


                for x, y in q:
                    visited[x][y] = 1 # 방문처리

                for x3 in range(1, N - 1):
                    for y3 in range(1, N - 1):
                        q2 = list()

                        q2.append([x3, y3])

                        for idx in range(4):
                            nx, ny = x3 + dx[idx], y3 + dy[idx]
                            q2.append([nx, ny])
                        
                        flag = False
                        for x, y in q2:
                            if visited[x][y] == 1:
                                flag = True
                        
                        if flag: continue

                        for x, y in q2:
                            visited[x][y] = 1 # 방문처리

                        candidate_sum = 0
                        for x in range(N):
                            for y in range(N):
                                if visited[x][y] == 1:
                                    candidate_sum += graph[x][y]
                        
                        answer = min(answer, candidate_sum)

                        for x, y in q2:
                            visited[x][y] = 0 # 원상복구
                for x, y in q:
                    visited[x][y] = 0        

print(answer)