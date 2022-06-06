# 크레인 인형뽑기 게임
def solution(board, moves):
    baguni = []
    answer = 0

    for i in moves:
        floor = 0
        while floor < len(board):
            if board[floor][i-1] == 0:
                floor += 1
            else:
                baguni.append(board[floor][i-1])
                board[floor][i-1] = 0 # 뽑았으므로
                break
        # 바구니 안 체크
        if len(baguni) >= 2:
            #같으면
            if baguni[-2] == baguni[-1]:
                baguni.pop()
                baguni.pop()
                answer += 2
    return answer


solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]],[1,5,3,5,1,2,1,4])