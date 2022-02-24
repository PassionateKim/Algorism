#체스판 다시 칠하기


N,M = map(int,input().split())

board = []
count = []

#이중배열 만들기
for i in range(N):
    board.append(input())

#8 x 8 돌리기
#행렬은 왼쪽 상단이 (0,0)임
#행
for y in range(N-7):
    #열
    for x in range(M-7):
        index = 0
        index2 = 0
        #8x8 
        for i in range(y,y+8):
            for j in range(x,x+8):
            #WBWBWBWB
            #BWBWBWBW에서 W인 것들의 공통점은 행 + 열의 값이 짝수라는 것
                if((i+j) % 2 == 0): #()?? 필수
                    if(board[i][j] != 'W'):
                        index += 1
                    if(board[i][j] != 'B'):
                        index2 += 1
                else:
                    if(board[i][j] != 'B'):
                        index += 1
                    if(board[i][j] != 'W'):
                        index2 += 1 
                
        count.append(min(index,index2))
i
print(min(count))


            
