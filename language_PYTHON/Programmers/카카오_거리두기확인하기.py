#2022-07-26
#카카오 거리두기 확인하기

dir = [(-1,0), (1,0), (0,-1), (0,1)]
dir2 = [(-2,0), (-1,1), (0,2), (1,1), (2,0), (1,-1), (0,-2), (-1,-1)]
def solution(places):
    answer = []
    # room으로 시작
    for room in places:
        flag = 1
        # room
        # 2차원 배열로 만들기
        graph = []
        for i in room:
            graph.append(list(map(str, i)))
        # /2차원 배열로 만들기

        # 세로, 가로 길이
        n = len(graph)
        m = len(graph[0])
        
        # p 위치 저장하기
        p_list = []
        for i in range(n):
            for j in range(m):
                if graph[i][j] == 'P':
                    p_list.append([i,j])
        
        # 대기자 없는 경우
        if len(p_list) == 0:
            answer.append(1)
            continue

        # 대기자 탐색 시작 - 맨해튼 거리 1, 2 이하
        for i in range(1, 3):
            for x, y in p_list:
                # 1. 맨해튼 거리가 1인 경우
                if i == 1:
                    for idx in range(4):
                        nx, ny = x + dir[idx][0], y + dir[idx][1]
                        if not (0<=nx<n and 0<=ny<m): continue # 범위 밖 X

                        # 맨해튼 거리 1 이내에 P가 존재하면
                        if graph[nx][ny] == 'P':
                            flag = 0
                            
                # 2. 맨해튼 거리가 2인 경우
                if i == 2:
                    for idx in range(8):
                        nx, ny = x + dir2[idx][0], y + dir2[idx][1]
                        if not (0<=nx<n and 0<=ny<m): continue # 범위 밖 X

                        # 맨해튼 거리 2이내에 P가 존재하면
                        if graph[nx][ny] == 'P':
                            # 직선인 경우
                            if idx % 2 == 0: 
                                kx, ky = nx - dir2[idx][0]//2, ny - dir2[idx][1]//2
                                # 뚫려있으면 거리두기를 지키지 않음
                                if graph[kx][ky] == 'O':
                                    flag = 0
                            # 대각선인 경우
                            if idx % 2 == 1:
                                kx, ky = x + dir2[idx][0], y
                                kx2, ky2 = x, y + dir2[idx][1]

                                if graph[kx][ky] == 'O' or graph[kx2][ky2] == 'O':
                                    flag = 0

        
        if flag == 0:
            answer.append(0)
        elif flag == 1:
            answer.append(1)


        # /room

    print(answer)
    return answer

# solution([["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"]])
solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
 ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
  ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], 
  ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], 
  ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]])