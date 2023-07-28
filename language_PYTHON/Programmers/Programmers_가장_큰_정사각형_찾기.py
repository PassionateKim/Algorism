# 복습 횟수:1, 00:30:00, 복습필요3
def solution(board):
    N = len(board)
    M = len(board[0])

    dp_table = [[0 for i in range(M)] for i in range(N)]

    for i in range(N):
        dp_table[i][0] = board[i][0]
    

    for i in range(M):
        dp_table[0][i] = board[0][i]

    for i in range(1, N):
        for j in range(1, M):
            if board[i][j] == 0: # 그냥 0인 경우
                dp_table[i][j] = 0
            else: # 1인 경우
                left_up = dp_table[i-1][j-1]
                up = dp_table[i-1][j]
                left = dp_table[i][j-1]

                if left_up == up == left:
                    dp_table[i][j] = left_up + 1
                else:
                    dp_table[i][j] = min(left_up, up, left) + 1
    
    answer = 0
    for i in range(N):
        for j in range(M):
            if dp_table[i][j] > answer:
                answer = dp_table[i][j]

    
    return answer


print(solution([[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]))