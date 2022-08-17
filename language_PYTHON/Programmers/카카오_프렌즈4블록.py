# 2022-08-17
# 카카오 프렌즈4블록
# 우 대각 하
dir = [(0,1), (1,1), (1,0)]
def solution(m, n, board):
    answer = 0
    n, m = m, n # 편의를 위해 기존 graph처럼 바꿈
    
    graph = []
    # 문자열2차원 배열로 치환
    for s in board:
        graph.append(list(s))
    
    
    while True:
        tuple_set = set()
        # 1. 체크하기
        for x in range(n):
            for y in range(m):
                tmp = graph[x][y]
                if tmp == '0': continue

                cnt = 1
                for idx in range(3):
                    nx, ny = x + dir[idx][0], y + dir[idx][1]
                    # 범위 벗어나면 X
                    if not (0<=nx<n and 0<=ny<m): continue
                    if tmp != graph[nx][ny]: continue
                    
                    cnt += 1

                # 만약 모두 같은 경우
                if cnt == 4:
                    tuple_set.add((x,y))
                    for idx in range(3):
                        nx, ny = x + dir[idx][0], y + dir[idx][1]
                        tuple_set.add((nx,ny))
        # ==탈출 조건==
        if len(tuple_set) == 0:
            break

        # ==ㅌ로직==
        # /1. 체크하기
        tuple_set = sorted(list(tuple_set)) # 디버깅 편의를 위해 


        # 초기화       
        while tuple_set:
            x, y = tuple_set.pop()
            answer += 1
            graph[x][y] = "0"
        
        # 2. 그래프 아래로 초기화
        for x in range(n-1,-1,-1):
            for y in range(m):
                if graph[x][y] == '0': continue
                
                tx, ty = x, y
                # 블록인 경우
                while True:
                    nx, ny = tx + dir[2][0], ty + dir[2][1]

                    if not (0<=nx<n and 0<=ny<m): break
                    if graph[nx][ny] != '0': break
                    # 뚫려있는 경우
                    if graph[nx][ny] == '0':
                        graph[nx][ny], graph[tx][ty] = graph[tx][ty], graph[nx][ny]
                        tx, ty = nx, ny  # 초기화
         
        #/2. 그래프 아래로 초기화
                     
        

    print(answer)
    return answer

solution(6,6,["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"])