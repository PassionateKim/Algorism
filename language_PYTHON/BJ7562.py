#나이트의 이동

from collections import deque
T= int(input())

#시계방향으로 돌리면서 체크

dx = [-1,-2,-2,-1,1,2,2,1]
dy = [-2,-1,1,2,2,1,-1,-2]

def BFS():
    queue = deque()
    x,y = present_location[0],present_location[1]
    queue.append([x,y])
    chess_place[x][y] = 1
    # for i in chess_place:
    #     print(i)
    while queue:
        x,y = queue.popleft()
        if(x ==purpose_location[0] and y == purpose_location[1]):
            print(chess_place[x][y] -1)
            return

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if(0<= nx < size and 0<= ny < size):
                #방문 체크
                if(chess_place[nx][ny] == 0):
                    chess_place[nx][ny] = chess_place[x][y] + 1
                    queue.append([nx,ny])
            
        # print("------------")
        # for i in chess_place:
        #     print(i)


for i in range(T):
    
    size = int(input())
    chess_place = [[0] * size for _ in range(size)]
    
    

    present_location = list(map(int,input().split()))
    purpose_location = list(map(int,input().split()))

    BFS()
    
    

    

    
