from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1 ,1]


def solution(board):
    answer = 0

    N = len(board)
    M = len(board[0])

    # start 초기화
    start = 0
    for i in range(N):
        for j in range(M):
            if board[i][j] == 'R':
                start = [i, j]
    
    visited = [[0 for i in range(M)] for i in range(N)]
    


    return answer



solution(["...D..R", ".D.G...", "....D.D", "D....D.", "..D...."]	)