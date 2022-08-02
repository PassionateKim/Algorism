# 2022-07-26
# 2022-07-29
# 2022-08-02
# 카카오 거리두기 확인하기

def solution(places):
    answer = []
    
    for pc in places:
        graph = []
        flag = 1
        # for 문 돌면서 2차원 배열 저장하기
        for hang in pc:
            graph.append(hang)
        
        # 행/열 길이 체크
        n = len(graph)
        m = len(graph[0])
        
        # p의 위치 저장하기
        p_list = []
        for i in range(n):
            for j in range(m):
                if graph[i][j] == 'P':
                    p_list.append([i,j])
        # 맨해튼 거리
        # 상하좌우
        dir = [(-1,0), (1,0), (0,-1), (0,1)]
        dir2 = [(-2,0), (2,0), (0,-2), (0,2)]
        dir3 = [(-1,-1), (-1,1), (1,-1), (1,1)]
        for p in p_list:
            x, y = p[0], p[1]
            # 맨해튼 1 
            for i in range(4):
                nx, ny = x + dir[i][0], y + dir[i][1]
                
                
                if not (0<=nx<n and 0<=ny<m): continue
                # 거리두기 X
                if graph[nx][ny] == 'P':
                    flag = 0
            
            # 맨해튼 2
            # 1. 상하좌우
            for i in range(4):
                nx, ny = x + dir2[i][0], y + dir2[i][1]
                if not (0<=nx<n and 0<=ny<m): continue
                # 거리두기 X
                if graph[nx][ny] == 'P':
                    kx, ky = x + dir[i][0], y + dir[i][1]
                    if graph[kx][ky] == 'O': # 칸이 아니면
                        flag = 0
            # 2. 대각선
            for i in range(4):
                nx, ny = x + dir3[i][0], y + dir3[i][1]
                if not (0<=nx<n and 0<=ny<m): continue
                # 거리두기 X
                if graph[nx][ny] == 'P':
                    kx, ky = x, y + dir3[i][1]
                    kx2, ky2 = x + dir3[i][0], y 
                    if graph[kx][ky] == 'O' or graph[kx2][ky2] == 'O':
                        flag = 0
            

        answer.append(flag)
    # /for pc
    print(answer)
    return answer


solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]])