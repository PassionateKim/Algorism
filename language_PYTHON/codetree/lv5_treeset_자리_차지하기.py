# 복습횟수:0, 01:30:00, 복습필요:***
from sortedcontainers import SortedSet
import sys
si = sys.stdin.readline
N, M = map(int, si().split())
arr = list(map(int, si().split()))

seats = SortedSet(range(1, M+1))

answer = 0

# 순서대로 앉히기
# 최선 = ai보다 같거나 작은 최대 위치 배치
for elem in arr:
    # ai보다 큰 최초의 위치
    idx = seats.bisect_right(elem)

    # 만약 큰 최초의 위치가
    # 첫 위치가 아니라면
    # 바로 전 위치가
    # ai보다 같거나 작은 최대 위치가 구해진다.
    if idx != 0:
        idx -= 1
        seats.remove(seats[idx])
        answer += 1
    else:
        break
    
print(answer)
# === 비교하기 ==== 
# # 복습횟수:0, 01:00:00, 복습필요:***
# from sortedcontainers import SortedSet
# import sys
# si = sys.stdin.readline
# N, M = map(int, si().split())
# s = SortedSet()

# arr_list = list(map(int, si().split()))
# if len(arr_list) == 1:
#     print(1)
# else:
#     for elem in arr_list:
#         if elem in s:
#             print(len(s))
#             break
#         s.add(elem)