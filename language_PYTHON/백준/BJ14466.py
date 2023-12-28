# 복습횟수:0
import sys
from collections import defaultdict
from collections import deque

si = sys.stdin.readline 
N, K, R = map(int, si().split())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

road_dict = defaultdict(list)
cow_list = list()

def road_init():
    for i in range(R):
        r1, c1, r2, c2 = map(int, si().split())
        road_dict[(r1-1, c1-1)].append((r2-1, c2-1))
        road_dict[(r2-1, c2-1)].append((r1-1, c1-1))

def cow_init():
    for i in range(K):
        x, y = map(int, si().split())
        cow_list.append([x-1, y-1])

road_init()
cow_init()
count = 0
# 특정 소가 갈 수 있는 모든 구역을 bfs로 탐색 
# 각 다음의 소듣의 위치가 bfs로 탐색된 것인지 체크
def bfs(x, y):
    q = deque()
    q.append([x, y])
    visited[x][y] = 1 # 방문처리
    
    while q:
        x, y = q.popleft()

        for idx in range(4):
            nx = x + dx[idx]
            ny = y + dy[idx]

            if not (0 <= nx < N and 0 <= ny < N): continue # 범위를 벗어난다면
            if visited[nx][ny] == 1: continue # 이미 방문한 경우라면

            if (nx, ny) in road_dict[(x, y)]: continue # 길이 있다면 

            q.append([nx, ny])
            visited[nx][ny] = 1 # 방문처리

    return

for index, cow in enumerate(cow_list):
    cow_x, cow_y = cow[0], cow[1] # cow's location

    visited = [[0 for i in range(N)] for i in range(N)]

    bfs(cow_x, cow_y)

    for next_cow in cow_list[index+1:]:
        next_cow_x, next_cow_y = next_cow[0], next_cow[1]

        if visited[next_cow_x][next_cow_y] == 0:
            count += 1

print(count)