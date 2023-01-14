# 강의실 배정
# 복습 횟수:0, 01:00:00
import sys
import heapq
si = sys.stdin.readline

N = int(si())

class_list = []
answer = [0]
for i in range(N):
    start, end = map(int, si().split())
    class_list.append([start, end])

# 일단 정렬 O(N)
class_list.sort(key=lambda x : (x[0], x[1]))

# O(N^2) 복잡도  약간 애매... -> 힙으로 변경 O(NlogN)
for start, end in class_list:
    # answer의 첫번쨰 index = 가장 작은 것과 비교
    if answer[0] <= start:
        heapq.heappop(answer)
    
    heapq.heappush(answer, end) # 만약에 사용할 수 없다면 강의실 추가
    
print(len(answer))