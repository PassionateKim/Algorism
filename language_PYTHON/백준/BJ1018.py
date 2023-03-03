#체스판 다시 칠하기
# 복습 횟수:2, 00:15:00, 복습필요X
import sys
si = sys.stdin.readline
answer = sys.maxsize
case1 = []
case2 = []
for i in range(8):
    if i % 2 == 0:
        case1.append(list('WBWBWBWB'))
    else:
        case1.append(list('BWBWBWBW'))

for i in range(8):
    if i % 2 == 0:
        case2.append(list('BWBWBWBW'))
    else:
        case2.append(list('WBWBWBWB'))

N, M = map(int, si().split())
graph = [list(map(str, si().strip())) for _ in range(N)]
def checkDiff(i, j):
    cnt1 = 0
    # case1 체크
    for x in range(8):
        for y in range(8):
            if case1[x][y] != graph[i + x][j + y]:
                cnt1 += 1
    
    cnt2 = 0
     # case2 체크
    for x in range(8):
        for y in range(8):
            if case2[x][y] != graph[i + x][j + y]:
                cnt2 += 1

    return min(cnt1, cnt2)

for i in range(N - 8 + 1):
    for j in range(M - 8 + 1):
        cnt = checkDiff(i, j)
        answer = min(answer, cnt)

print(answer)