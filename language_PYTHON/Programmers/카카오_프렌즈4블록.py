# 2022-08-17
# 2022-08-24
# 카카오 프렌즈4블록
dir = [(0,1), (1,1), (1,0)]
def solution(m, n, board):
    answer = 0
    graph = []

    # 2차원 그래프로 변경
    for i in board:
        graph.append(list(i))

    # 전체 탐색
    while True:
        location_set = set()
        # 1. 정사각형 탐색
        for x in range(m):
            for y in range(n):
                if graph[x][y] == '0' :continue
                check = graph[x][y]
                cnt = 1
                for idx in range(3):
                    nx, ny = x + dir[idx][0], y + dir[idx][1]
                    if not (0<=nx<m and 0<=ny<n): continue

                    if graph[nx][ny] == check:
                        cnt += 1
                # 만약 cnt 4라면 정사각형을 만족하므로
                if cnt == 4:
                    location_set.add((x,y))
                    for idx in range(3):
                        nx, ny = x + dir[idx][0], y + dir[idx][1]
                        location_set.add((nx, ny))
        # / 1. 정사각형 탐색

        # ==탈출조건==
        if not location_set:
            break
        # 2. 초기화
        while location_set:
            answer += 1
            x, y = location_set.pop()
            graph[x][y] = '0'
        # / 2. 초기화
        # 3. 아래로 내리기 - 아래부터 탐색
        for x in range(m-1,-1,-1):
            for y in range(n):
                if graph[x][y] == '0': continue
                kx, ky = x, y
                while True:
                    nx, ny = kx + 1, y
                    
                    if not (0<=nx<m and 0<=ny<n): break
                    if graph[nx][ny] != '0': break

                    graph[kx][ky], graph[nx][ny] = graph[nx][ny], graph[kx][ky]
                    
                    kx, ky = nx, ny
        # /3. 아래로 내리기
    print(answer)       
    return answer

solution(6,6,["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"])