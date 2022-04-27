# 공유기 설치
import sys
N,C = map(int,input().split())
answer = 0
location_list = []
for i in range(N):
    location_list.append(int(sys.stdin.readline().rstrip()))

#정렬하기 for 이분 탐색
location_list = sorted(location_list)
answer = 0
def Binary(start, end):
    global answer
    while start <= end:
        count = 1
        current = location_list[0]
        mid = (start + end) // 2
        
        print(start, end, mid)
        for i in range(1, len(location_list)):
            # 체크하기
            if location_list[i] - current >= mid:
                count += 1
                current = location_list[i]
            
        if count < C: #count가 작으면 범위를 줄여야함 
            end = mid - 1
        else:
            start = mid + 1
            answer = mid


 
Binary(1, location_list[-1] - location_list[0])
print(answer)