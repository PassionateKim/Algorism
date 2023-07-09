# 복습 횟수:0, 00:30:00, 복습필요O
# 시간 복잡도 O(N)에 끝내야 한다. 
import sys 
si = sys.stdin.readline

N, M = map(int, si().split())

zari_list = [i for i in range(N+1)]
location_set_list = [set() for i in range(N+1)]
for i in range(1, len(location_set_list)):
    location_set_list[i].add(i)

switch_table = []
for i in range(M):
    x, y = map(int, si().split())
    switch_table.append([x, y])

for i in range(3):
    for s_x, s_y in switch_table:
        before_zari1, before_zari2 = zari_list[s_x], zari_list[s_y] # 1, 3

        # swap
        tmp = zari_list[s_x]
        zari_list[s_x] = zari_list[s_y]
        zari_list[s_y] = tmp
        # 3, 1

        # 위치 저장
        if(s_x not in location_set_list[before_zari2]):
            location_set_list[before_zari2].add(s_x)
        
        if(s_y not in location_set_list[before_zari1]):
            location_set_list[before_zari1].add(s_y)

for i in range(1, len(location_set_list)):
    print(len(location_set_list[i]))