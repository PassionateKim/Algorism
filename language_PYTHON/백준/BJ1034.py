# 2022-08-22
# 램프
import sys
si = sys.stdin.readline

answer = 0
N, M = map(int, si().split())
graph = []
for i in range(N):
    graph.append(list(map(int, si().strip())))

Z = int(si())

# 1) 0의 개수 구하기
zero_list = []

for hang in graph:
    cnt = 0
    for i in hang:
        if i == 0:
            cnt += 1
    zero_list.append(cnt)

# 2) 행 돌면서 최대값 구해보기
for zero, hang in zip(zero_list, graph):
    # 크면 어차피 못만드니 pass
    if zero > Z: continue
    # 나머지가 동일하지 않다면 어차피 못만드니 pass
    if zero % 2 != Z % 2: continue

    candidate = 0 
    for idx, hang2 in enumerate(graph):
        if hang == hang2:
            candidate += 1
    answer = max(candidate, answer)

print(answer)