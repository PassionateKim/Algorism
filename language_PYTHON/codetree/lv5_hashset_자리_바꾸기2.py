# 2023-07-13
# 복습 횟수:1, 01:00:00, 복습필요:**
# 시간 복잡도 O(N)에 끝내야 한다. 
import sys 
si = sys.stdin.readline

N, M = map(int, si().split())
seat_list = [i for i in range(N+1)]

seat_set = dict()

for i in range(N):
    seat_set[i+1] = set()
    seat_set[i+1].add(i+1)

switch_table = []
for i in range(M):
    x, y = map(int, si().split()) # location
    switch_table.append([x, y])
    
for i in range(3):
    for i in range(M):
        x, y = switch_table[i]

        tmp = seat_list[x]
        seat_list[x] = seat_list[y] # 3
        seat_list[y] = tmp # 1

        if y not in seat_set[seat_list[y]]:
            seat_set[seat_list[y]].add(y)

        if x not in seat_set[seat_list[x]]:
            seat_set[seat_list[x]].add(x) 

for i in range(1, N+1):
    print(len(seat_set[i]))