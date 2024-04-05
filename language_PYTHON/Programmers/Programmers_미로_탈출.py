from collections import deque 

dx = [-1, 1, 0 ,0]
dy = [0, 0, -1, 1]


def bfs(s_x, s_y, e_x, e_y, l_x, l_y, visited: list, maps: list):
    
    q = deque()
    # x, y, isLeverVisited
    q.append([s_x, s_y, False, 0])
    visited[s_x][s_y][0] = 1 # 방문처리

    while q:
        x, y, isLever, count = q.popleft()
        # 레버를 갖고 END 지점에 도달한 경우
        if isLever and x == e_x and y == e_y:
            return count
        
        if isLever:
            for idx in range(4):
                nx, ny = x + dx[idx], y + dy[idx]
                # 범위를 넘어가는 경우
                if not (0 <= nx < len(visited) and 0 <= ny < len(visited[0])): continue
                
                # 벽이거나, 이미 방문한 경우
                if maps[nx][ny] == 'X' or visited[nx][ny][1] == 1: continue

                q.append([nx, ny, True, count + 1])
                visited[nx][ny][1] = 1 # 방문처리

        if not isLever:
            for idx in range(4):
                nx, ny = x + dx[idx], y + dy[idx]
                # 범위를 넘어가는 경우
                if not (0 <= nx < len(visited) and 0 <= ny < len(visited[0])): continue

                # 벽이거나, 이미 방문한 경우
                if maps[nx][ny] == 'X' or visited[nx][ny][0] == 1: continue

                visited[nx][ny][0] = 1 # 방문처리
                check = False
                if maps[nx][ny] == 'L':
                    check = True

                if check:    
                    visited[nx][ny][1] = 1 # 방문처리
                q.append([nx, ny, check, count + 1])                
    
    return -1

def solution(maps):
    
    answer = 0
    start = 0
    end = 0
    lever = 0
    visited =[[[0, 0] for i in range(len(maps[0]))] for i in range(len(maps))]

    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == 'S':
                start = [i, j]
            
            if maps[i][j] == 'E':
                end = [i, j]
            
            if maps[i][j] == 'L':
                lever = [i, j]

    answer = bfs(start[0], start[1], end[0], end[1], lever[0], lever[1], visited, maps)
    
    return answer


solution(["SOOOL","XXXXO","OOOOO","OXXXX","OOOOE"])
solution(["LOOXS","OOOOX","OOOOO","OOOOO","EOOOO"])
solution(["LOOS", "OOOO", "OOOO", "OOOO", "OOOE"])

