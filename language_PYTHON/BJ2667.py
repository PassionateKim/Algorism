import sys
from collections import deque

N = int(input())
graph = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)]
visited =[[0] * N for _ in range(N)]

# 상하좌우
dx = [-1,1,0,0]
dy = [0,0,-1,1]

answer_list = [] # 최종 정답
cnt = 1 # 단지번호 및 개수
answer = 0 # 단지 당 개수

def bfs(x, y):
    global cnt
    global answer 

    q = deque()
    q.append([x,y])
    visited[x][y] = cnt # 방문처리
    answer += 1 # 추가

    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (0 <= nx < N and 0 <= ny < N): # 그래프 내
                if graph[nx][ny] == 1 and visited[nx][ny] == 0:
                    q.append([nx,ny])
                    visited[nx][ny] = 1 # 방문처리
                    answer += 1 # 추가

    
    
    


for i in range(N):
    for j in range(N):
        if graph[i][j] == 1 and visited[i][j] == 0: # 아파트 단지 && 방문 X
            bfs(i, j)
            cnt += 1
            answer_list.append(answer)
            answer = 0
      
print(len(answer_list))
answer_list.sort() # 오름차순으로 정리하시오
for i in answer_list:
    print(i)
