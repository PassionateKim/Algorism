# 복습 횟수:0, 01:00:00, 복습필요O
def solution(board):
    answer = 0
    n = len(board)
    m = len(board[0])
    new_board = [[0 for _ in range(m+1)] for _ in range(n+1)]
    
    for i in range(n):
        for j in range(m):
            new_board[i+1][j+1] = board[i][j]
    
    for i in range(1, n+1):
        for j in range(1, m+1):
            if new_board[i][j] == 1:
                new_board[i][j] = min(new_board[i][j-1], new_board[i-1][j], new_board[i-1][j-1]) + 1
                answer = max(answer, new_board[i][j] ** 2)
    
    return answer

solution([[1]])