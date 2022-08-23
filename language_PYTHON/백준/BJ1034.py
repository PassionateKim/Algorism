# 2022-08-22
# 2022-08-23
# 램프
import sys
si = sys.stdin.readline

answer = 0
N, M = map(int, si().split())
graph = []
for i in range(N):
    graph.append(list(map(int, si().strip())))

Z = int(si())
zero_list = list() 
# 1. 0의 개수 구하기
for hang in graph:
    tmp = 0
    for i in hang:
        if i == 0:
            tmp += 1
    zero_list.append(tmp)

# 2. 행 돌면서 체크하기
for zero, hang in zip(zero_list, graph):
    # 예외 처리
    if zero % 2 != Z % 2: continue
    if zero > Z: continue
    cnt = 0
    for hang2 in graph:
        if hang == hang2:
            cnt += 1
    answer = max(answer ,cnt)
print(answer)