# 2022-08-22
# 2022-08-23
# 2022-08-29
# 램프
import sys
si = sys.stdin.readline
N, M = map(int, si().split())
answer = 0
graph = []
for i in range(N):
    graph.append(list(map(int, si().strip())))

K = int(si())

zero_list = []

for hang in graph:
    cnt = 0
    for i in hang:
        if i == 0:
            cnt += 1
    zero_list.append(cnt)

for zero, hang in zip(zero_list, graph):
    # 홀짝이 맞아야함
    if zero % 2 != K % 2: continue
    # zero가 더 크면 행을 완성할 수 없음
    if zero > K: continue

    tmp = 0
    print("hang", hang)
    for hang2 in graph:
        print("hang2", hang2)
        if hang == hang2:
            tmp += 1
    print("tmp",tmp)
    answer = max(answer , tmp)
    
print(answer)