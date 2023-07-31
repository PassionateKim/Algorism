# 미네랄 
# 복습 횟수:2, 02:00:00, 복습필요3
import sys
from collections import deque
si = sys.stdin.readline 
R, C = map(int, si().split())
graph = []

for i in range(R):
    tmp = list(map(str, si().rstrip()))
    graph.append(tmp)

N = int(si())
height_list = list(map(int, si().split()))


# 떠 있다는 것을 어떻게 체크할 것인가??
# BFS()로 [0]에 닿는지 안 닿는지를 체크
def delete_mineral(check_left_right):
    # 왼쪽 오른쪽에 따라 삭제
    if check_left_right == 1: # 왼쪽인 경우
        index = 0
        while True:
            if index == C:
                break
            if graph[height][index] == 'x':
                graph[height][index] = '.'
                return [height, index]
            else:
                index += 1
    else:
        index = C-1
        while True:
            if index == -1:
                break

            if graph[height][index] == 'x':
                graph[height][index] = '.'
                return [height, index]
            else:
                index -= 1

    return [-1, -1]

def bfs(x, y):
    flag = True
    q = deque() 
    q.append([x, y])
    visited[x][y] = 1 # 방문처리

    while q:
        x, y = q.popleft()
        if x == R-1: # 연결된 것이 땅에 닿으면 cluster가 아니므로
            flag = False

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if not (0 <= nx < R and 0 <= ny < C): continue

            if visited[nx][ny] == 0 and graph[nx][ny] == 'x':
                q.append([nx, ny])
                visited[nx][ny] = 1

    return flag
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

check_left_right = 1
for height in height_list:  
    height = R - height # 우리의 좌표 x, y 에 맞추기 

    # 왼쪽 오른쪽에 따라 mineral 삭제
    check_break = delete_mineral(check_left_right)
    # 왼쪽 오른쪽 변경
    check_left_right = (-1) * check_left_right

    # mineral 모양 체크
    if check_break != [-1, -1]: #삭제된 것이 존재하는 경우
        # 4 방향 체크 candidate
        x, y = check_break
        for idx in range(4):
            nx, ny = x + dx[idx], y + dy[idx]
            if not (0 <= nx < R and 0 <= ny < C): continue
            if graph[nx][ny] == '.': continue # cluster인지를 체크해야하므로
            visited = [[0 for i in range(C)] for i in range(R)]
            isCluster = bfs(nx, ny)

            if isCluster:
                break
        
        # 내리기
        if isCluster: # Cluster가 존재하는 경우
            down_point = 1000

            for i in range(R):
                for j in range(C):
                    if visited[i][j] == 1: # 
                       tmp = 0
                       cnt = 1
                       while True:
                            if visited[i+cnt][j] == 1: # 같은 무리라면
                                break
                            
                            if graph[i+cnt][j] == 'x': # 종료
                                down_point = min(down_point, tmp)
                                break

                            if i+cnt == R-1:
                                down_point = min(down_point, cnt)
                                break

                            if visited[i+cnt][j] != 1 and graph[i+cnt][j] == '.': # 같은 무리가 아니고 내려갈 수 있으면
                                tmp += 1
                                cnt += 1
                            
                            
            
            for i in range(R-1, -1, -1):
                for j in range(C):
                    if visited[i][j] == 1: 
                        graph[i+down_point][j] = graph[i][j]
                        graph[i][j] = '.'


for i in graph:
    print("".join(i))