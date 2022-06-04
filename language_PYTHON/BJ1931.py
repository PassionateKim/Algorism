# #회의실 배정
import sys
N = int(input())
convention = [tuple(map(int, input().split())) for _ in range(N)]
convention.sort(key = lambda x: (x[1], x[0]))
cnt = 1
current = convention[0][1]
for i in range(1, len(convention)):
    if convention[i][0] >= current:
        current = convention[i][1] 
        cnt += 1

print(cnt)