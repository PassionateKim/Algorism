# 공유기 설치
from array import array
import sys
N,C = map(int,input().split())
answer = 0
location_list = []
for i in range(N):
    location_list.append(int(sys.stdin.readline().rstrip()))

#정렬하기 for 이분 탐색
location_list = sorted(location_list)

def Binary(start, end):
    print(start, end, (start+end) // 2)
    global answer
    if start > end:
        return
    count = 1 
    mid = (start + end) // 2
    current = location_list[0]

    for i in range(1,len(location_list)):
        if location_list[i] - current >= mid:
            count += 1
            current = location_list[i]
    print(count)
    if count <= C: # 개수가 적으면 값을 줄여야 하므로
        return Binary(start, mid -1)
    else:
        answer = mid 
        return Binary(mid+1, end)
     

Binary(1, location_list[-1] - location_list[0])
print(answer)