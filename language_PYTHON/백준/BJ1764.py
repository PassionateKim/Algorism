# 듣보잡 
import sys
si = sys.stdin.readline
N, M = map(int, si().split())

listen_list = []
see_list = []

for i in range(N):
    listen_list.append(si().strip())

for i in range(M):
    see_list.append(si().strip())
    
listen_list.sort() # 이분 탐색을 위한 정렬

def Binary(start, end, target):
    while start<=end:
        mid = (start + end) // 2    
        if listen_list[mid] == target:
            answer.append(listen_list[mid])
            return

        if listen_list[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return

answer = []

for i in see_list:
    Binary(0,len(listen_list)-1, i)

# 출력값
print(len(answer))
for i in answer:
    print(i)