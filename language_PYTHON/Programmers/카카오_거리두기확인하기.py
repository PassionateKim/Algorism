# 2022-07-26
# 2022-07-29
# 2022-08-02
# 2022-08-09
# 카카오 거리두기 확인하기

def solution(places):
    answer = []
    for place in places:
        flag = 1
        graph = []
        p_list = []
        # 1. place 별 체크 시작
        for hang in place:
            # graph 초기화하기
            graph.append(list(map(str, hang)))
        
        n = len(graph)
        m = len(graph[0])
        # p 위치 저장하기
        for i in range(n):
            for j in range(m):
                if graph[i][j] == 'P':
                    p_list.append([i, j])
        
        # 체크하기
        # 맨해튼 거리 1
        dir = [(-1,0), (1,0), (0,-1), (0,1)]
        for p in p_list:
            x, y = p[0], p[1]
            for i in range(4):
                nx, ny = x + dir[i][0], y + dir[i][1]
                if not (0<=nx<n and 0<=ny<m): continue
                
                # 거리두기가 지켜지지 않는 경우
                if graph[nx][ny] == 'P':
                    flag = 0
        
        # 맨해튼 거리 2-1
        dir2 = [(-2,0), (2,0), (0,-2), (0,2)]
        for p in p_list:
            x, y = p[0], p[1]
            for i in range(4):
                nx, ny = x + dir2[i][0], y + dir2[i][1]
                if not (0<=nx<n and 0<=ny<m) : continue
            
                # 거리에 P 있는지 체크
                if graph[nx][ny] == 'P':
                    kx, ky = (x + nx)//2, (y+ny)//2
                    # 있는데, 뚫려있다면 거리두기 지키지 않은 것이므로
                    if graph[kx][ky] == 'O':
                        flag = 0
        # 맨해튼 거리 2-2
        dir3 = [(-1,-1), (-1,1), (1,-1), (1,1)]
        for p in p_list:
            x, y = p[0], p[1]
            for i in range(4):
                nx, ny = x + dir3[i][0], y + dir3[i][1]
                if not (0<=nx<n and 0<=ny<m): continue
                # 거리에 P 있는지 체크
                if graph[nx][ny] == 'P':
                    kx, ky = x + dir3[i][0], y
                    kx2, ky2 = x, y + dir3[i][1]
                    
                    if (graph[kx][ky] == 'O' or graph[kx2][ky2] == 'O'):
                        flag = 0


        # /place
        if flag == 1:
            answer.append(1)
        else:
            answer.append(0)                    
        print(answer)
        exit()
        
    return answer


solution([["POOOO", "XPXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]])