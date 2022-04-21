#로봇
import sys
from collections import deque
input = sys.stdin.readline
M, N = map(int, input().split())
miro = [list(map(int, input().split())) for _ in range(M)]
start_r, start_c, start_dir = map(int, input().split())
end_r, end_c, end_dir = map(int, input().split())
# 문제에서 동 서 남 북 1 2 3 4
dr = [0, 0, 0, 1, -1]  # 행 동 서 남 북
dc = [0, 1, -1, 0, 0]  # 열 동 서 남 북
result = 0  # 결과를 출력할 변수
# 각각의 좌표에 대하여 동서남북 4가지 방향으로 방문처리
visited = [[[False] * 5 for _ in range(N)] for _ in range(M)]
def bfs(r, c, s_dir):
    global result
    queue = deque([[r, c, s_dir, 0]])
    visited[r][c][s_dir] = True
    while queue:
        print(queue)
        r, c, c_dir, count = queue.popleft()
        # 만약 도착지점에 도착했다면 횟수 저장후 종료
        if r == end_r - 1 and c == end_c - 1 and c_dir == end_dir:
            result = count
            return
        for i in range(1, 3 + 1):  # 1,2,3 칸을 차례대로 이동한다
            nr = r + (dr[c_dir] * i)
            nc = c + (dc[c_dir] * i)
            # 만약 범위를 벗어나거나 이미 방문했다면 continue
            if nr < 0 or nr >= M or nc < 0 or nc >= N or visited[nr][nc][c_dir]:
                continue
            if miro[nr][nc] == 1:  # 만약 1이 껴있으면 2~3칸은 이동할 수 없으므로 break
                break
            visited[nr][nc][c_dir] = True  # 방문처리
            queue.append([nr, nc, c_dir, count + 1])  # 횟수를 늘려 큐에 담아준다.
        if c_dir == 1 or c_dir == 2:  # 현재가 동,서방향일 때
            if not visited[r][c][3]:  # 남쪽방향을 아직 방문하지 않았다면
                visited[r][c][3] = True  # 방문처리 후 큐에 넣기
                queue.append([r, c, 3, count + 1])
            if not visited[r][c][4]:  # 북쪽방향을 아직 방문하지 않았다면
                visited[r][c][4] = True
                queue.append([r, c, 4, count + 1])
        else:  # 현재가 남,북방향일 때
            if not visited[r][c][1]:  # 동쪽방향을 아직 방문하지 않았다면
                visited[r][c][1] = True
                queue.append([r, c, 1, count + 1])
            if not visited[r][c][2]:  # 서쪽방향을 아직 방문하지 않았다면
                visited[r][c][2] = True
                queue.append([r, c, 2, count + 1])
bfs(start_r - 1, start_c - 1, start_dir)
print(result)





# M,N = map(int,input().split())
# factory_graph = []
# visited = [[[0] * 2 for _ in range(N)] for _ in range(M)]




# #상하좌우
# dx = [-1,1,0,0]
# dy = [0,0,-1,1]


# for i in range(M):
#     factory_graph.append(list(map(int,sys.stdin.readline().split())))

# start_point = list(map(int,sys.stdin.readline().split()))
# end_point = list(map(int,sys.stdin.readline().split()))

# def way(a,b):
#     #방향이 같은 경우
#     if a == b:
#         return 0
#     #a가 북쪽인 경우
#     elif a == 4:
#         # b가 동,서쪽인 경우
#         if b == 1 or b == 2:
#             return 1
#         #남쪽인 경우
#         else:
#             return 2
#     #a가 남쪽인 경우
#     elif a == 3:
#         #b가 동,서쪽인 경우
#         if b == 1 or b == 2:
#             return 1
#         #북쪽인 경우
#         else:
#             return 2
#     #a가 서쪽인 경우
#     elif a == 2:
#         #b가 북쪽,남쪽인 경우
#         if b == 4 or b == 3:
#             return 1
#         #b가 서쪽인 경우
#         else:
#             return 2
#     #a가 동쪽인 경우
#     else:
#         #b가 북쪽,남쪽인 경우
#         if b == 4 or b == 3:
#             return 1
#         #b가 서쪽인 경우
#         else:
#             return 2        

# def BFS(x,y,direction):
#     q = deque()
#     q.append([x,y,direction])
#     #시작점 방문
#     visited[x][y][0] = 1
#     #start 지점과 end 지점이 똑같은 경우
#     if x == end_point[0] - 1 and y == end_point[1] - 1:
#         value = way(end_point[2], start_point[2])
#         print(value)
#         return 
    
#     while q:
#         print(q)
#         x,y,direction = q.popleft()
#         if x == end_point[0] - 1 and y == end_point[1] - 1:
#             print(visited[x][y][0] - 1 + way(direction,end_point[2]))
#             return

#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]

#             #사이즈 안쪽으로
#             if (0<= nx <M and 0<= ny <N):
#                 #길이 뚫려있다 && 방문하지 않았다.
#                 if factory_graph[nx][ny] == 0 and visited[nx][ny][0] == 0:
#                     #뚫려 있는 것이 북쪽인 경우
#                     if nx == x - 1:
#                         differ = way(4, direction)
#                         visited[nx][ny][0] = visited[x][y][0] + 1 + differ
#                         q.append([nx,ny,4])
#                     #뚫려 있는 것이 남쪽인 경우
#                     elif nx == x + 1:
#                         differ = way(3, direction)
#                         visited[nx][ny][0] = visited[x][y][0] + 1 + differ
#                         q.append([nx,ny,3])
#                     #뚫려 있는 것이 서쪽인 경우
#                     elif ny == y - 1:
#                         differ = way(2, direction)
#                         visited[nx][ny][0] = visited[x][y][0] + 1 + differ
#                         q.append([nx,ny,2])
#                     #뚫려 있는 것이 동쪽인 경우
#                     else:
#                         differ = way(1, direction)
#                         visited[nx][ny][0] = visited[x][y][0] + 1 + differ
#                         q.append([nx,ny,1])

#                     #방향을 틀고 앞으로 나아가기 시작할 때 
#                     if differ == 0:
#                         visited[nx][ny][1] = visited[x][y][1] + 1
#                     #돌고 같은 방향인 경우
                    
                    
                        
#                     # #명령 1.Go k: k는 1, 2 또는 3일 수 있다.
#                     # # 방향을 바꾸면서 움직이는 경우에 초기화 
                    
#                     #체크하기
#                     # print("------------")
#                     # for i in visited:
#                     #     print(i)
                  
                
                    
# #index 이므로                 
# BFS(start_point[0] - 1, start_point[1] - 1, start_point[2])
