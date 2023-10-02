# 복습횟수:1, 00:30:00, 복습필요2

import sys
si = sys.stdin.readline 
N = int(si())
target_list = list(map(int, si().split()))
remember = target_list[:]

for i in range(len(target_list) -1, 0, -1):
    if target_list[i-1] < target_list[i]:
        for j in range(len(target_list)-1 , 0, -1):
            if target_list[j] > target_list[i-1]:
                # swap 해야함
                tmp = target_list[i-1]
                target_list[i-1] = target_list[j]
                target_list[j] = tmp
                break
        target_list = target_list[:i] + sorted(target_list[i:])
        break

if remember == target_list:
    print(-1)
else:
    print(*target_list)