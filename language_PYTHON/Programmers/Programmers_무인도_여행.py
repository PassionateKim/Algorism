from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, graph: list, visited: list):
    location_list = []

    N = len(graph)
    M = len(graph[0])

    q = deque()
    q.append([x, y])
    visited[x][y] = 1 
    while q:
        x, y = q.popleft()
        location_list.append(int(graph[x][y]))

        for idx in range(4):
            nx, ny = x + dx[idx], y + dy[idx]

            if not (0 <= nx < N and 0 <= ny < M): continue
            if visited[nx][ny] == 1: continue
            if graph[nx][ny] == 'X': continue

            q.append([nx, ny])
            visited[nx][ny] = 1 # 방문처리

    return sum(location_list)

def solution(maps):
    answer = []

    N = len(maps)
    M = len(maps[0])

    visited = [[0 for i in range(M)]for i in range(N)]
    graph = []

    for map in maps:
        graph.append(map)

    for i in range(N):
        for j in range(M):

            if visited[i][j] == 1 or graph[i][j] == 'X': continue
            
            answer.append(bfs(i, j, graph, visited))
    
    answer.sort()
    
    return answer


solution(["XXX","XXX","XXX"])