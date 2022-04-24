from collections import deque
dr = [-1, 0, 1, 0]  # 상 우 하 좌
dc = [0, 1, 0, -1]  # 상 우 하 좌

def BFS(visited):
    global answer 
    queue = deque([[0,0]])
    visited[0][0] = True
    
    while queue:
        r, c = queue.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            # 평면도 범위 내 && 벽이 아닐 때 && 방문하지 않았을 때
            if 0 <= nr < h+2 and 0 <= nc < w+2 and miro[nr][nc] !="*" and not visited[nr][nc]:
                if 'A' <= miro[nr][nc] <= 'Z': # 문인 경우
                    if chr(ord(miro[nr][nc]) + 32) not in key: # 해당 문을 열 키가 없는 경우
                        continue # 방문하지 않는다.
                elif 'a' <= miro[nr][nc] <= 'z': # 키인 경우
                    if miro[nr][nc] not in key:
                        key[miro[nr][nc]] = True # 키 저장
                        visited = [[False] * (w+2) for _ in range(h+2)] # 초기화
                elif miro[nr][nc] == "$": # 문서인 경우
                    if (nr, nc) not in visited_doc:
                        visited_doc.append((nr, nc)) #방문 문서 체크
                        answer += 1 
                # else는 생략 어차피 지나가는 것이므로
                visited[nr][nc] = True
                queue.append([nr, nc])

                 


                


T = int(input())
for _ in range(T):
    h, w = map(int, input().split())
    miro = ["." + input() + "." for _ in range(h)]
    miro = ["." * (w+2)] + miro + ["." * (w+2)]
    visited = [[False] * (w+2) for _ in range(h)]
    key = {} # 가지고 있는 키 저장
    visited_doc = [] # 방문한 키 위치 저장
    for i in input():
        if i.isalpha(): # 만약 알파벳이면
            key[i] = True # 키 저장
    answer = 0
    BFS(visited)
    print(answer)    
   
# def bfs(visited):
#     global ans
#     queue = deque([[0, 0]])
#     visited[0][0] = True
#     while queue:
#         r, c = queue.popleft()
#         for i in range(4):
#             nr = r + dr[i]
#             nc = c + dc[i]
#             # 범위를 벗어나거나 벽이거나 이미 방문했다면 컨티뉴
#             if nc < 0 or nc >= w + 2 or nr < 0 or nr >= h + 2 or miro[nr][nc] == '*' or visited[nr][nc]:
#                 continue
#             if 'A' <= miro[nr][nc] <= 'Z':  # 대문자라면(문이라면)
#                 if chr(ord(miro[nr][nc]) + 32) not in key:  # 해당 문을 열수있는 키가 없다면
#                     continue  # 컨티뉴
#             elif 'a' <= miro[nr][nc] <= 'z':  # 만약 소문자이고
#                 if miro[nr][nc] not in key:  # 아직 키에 없다면
#                     key[miro[nr][nc]] = True  # 해당 키를 저장후
#                     visited = [[False] * (w + 2) for _ in range(h + 2)]  # 방문체크 초기화
#             elif miro[nr][nc] == "$" and (nr, nc) not in visited_doc:  # 비밀문서이고 아직방문하지 않았다면
#                 ans += 1  # 찾은 개수 1개 증가
#                 visited_doc.append((nr, nc))  # 해당 위치는 더이상 방문하면 안되기 때문에 저장
#             visited[nr][nc] = True  # 방문처리
#             queue.append([nr, nc])  # 다음 위치를 큐에 삽입

# T = int(input())
# for _ in range(1, T + 1):
#     h, w = map(int, input().split())
#     miro = ['.' + input() + '.' for _ in range(h)]
#     miro = ['.' * (w + 2)] + miro + ['.' * (w + 2)]
#     visited = [[False] * (w + 2) for _ in range(h + 2)]
#     key = {}  # 가지고 있는 키 저장
#     visited_doc = []  # 방문한 키 위치 저장
#     for i in input():
#         if i.isalpha():  # 만약 알파벳이면
#             key[i] = True  # 키로 저장
#     ans = 0
#     bfs(visited)
#     print(ans)


# for i in miro:
#     print(i)



# #열쇠
# from collections import deque
# import sys

# input = sys.stdin.readline
# answer = []
# #상하좌우
# dh = [-1,1,0,0]
# dw = [0,0,-1,1]


# def BFS():
#     result = 0
#     while queue:
#         h,w = queue.popleft()
#         for i in range(4):
#             nh = h + dh[i]
#             nw = w + dw[i]

        
#     print(result)

        




# for i in range(int(input())):
#     h, w = map(int,input().split())
#     queue = deque()
#     board = [list(input().rstrip()) for _ in range(h)]    
#     keys = list(input().rstrip())
#     visited = [[0 for _ in range(w)] for _ in range(h)]

#     # 시작 포인트 
#     for i in range(h):
#         for j in range(w):
#             if (i == 0 or i == h-1 or j == 0 or j == w-1) and board[i][j] != "*": # 가장자리의 벽에서 시작
#                 queue.append([i,j]) # 시작할 수 있는 포인트 일단 get
#                 visited[i][j] = 1 # door 방문처리
    
#     BFS()
    






    
    
