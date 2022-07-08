#체스판 다시 칠하기
import sys
si = sys.stdin.readline

N, M = map(int, si().split())
graph = []

for i in range(N):
    graph.append(list(si()))

answer = 1e5 # 최대 50 * 50

for i in range((N-8) + 1):
    for j in range((M-8) + 1):
        white_start, black_start = 0, 0
        
        for x in range(8): # 8*8 돌기
            for y in range(8):
                nx, ny = x + i, y + j
                #시작
                if (nx + ny) % 2 == 0: 
                    if graph[nx][ny] == 'B': # white 여야 하는 부분
                        white_start += 1
                    elif graph[nx][ny] == 'W': # black 이어야 하는 부분
                        black_start += 1
                else: 
                    if graph[nx][ny] == 'W':
                        white_start += 1 # black이어야하는부분
                    elif graph[nx][ny] == 'B':
                        black_start += 1 # white이어야하는부분
                
                #// y
        if answer > min(white_start, black_start):
            answer = min(white_start, black_start)

print(answer)





        
                
            
