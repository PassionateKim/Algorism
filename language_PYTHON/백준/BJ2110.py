# 공유기 설치
import sys

si = sys.stdin.readline
N, C = map(int, si().split())

homes = []
for i in range(N):
    homes.append(int(si()))

homes.sort()

def Binary(start, end):
    answer = 0
    while start<=end:
        count = 1
        current = homes[0]
        mid = (start + end) // 2

        for i in range(1, len(homes)): 
            if homes[i] - current >= mid:
                count += 1
                current = homes[i]
        
        if count >= C:
            start = mid + 1
            answer = mid
        else:
            end = mid - 1
    return answer

print(Binary(1, homes[-1] - homes[0]))
        
