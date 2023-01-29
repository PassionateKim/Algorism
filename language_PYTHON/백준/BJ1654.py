# 랜선 자르기
# 복습 횟수:2
import sys
si = sys.stdin.readline
K, N = map(int, si().split())
line_list = []
for i in range(K):
    line_list.append(int(si()))
answer = 0
def binary(start, end, target):
    global answer
    while start <= end:
        mid = (start + end) // 2
        tmp = 0
        for line in line_list:
            tmp += (line // mid)
        
        if tmp >= target:
            answer = mid
            start = mid + 1
        else:
            end = mid - 1

    return

binary(1, max(line_list), N)
print(answer)