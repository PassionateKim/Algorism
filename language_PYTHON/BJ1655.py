#가운데를 말해요
import sys
import heapq
input = sys.stdin.readline

N = int(input())
left_heap = []
right_heap = []

for i in range(N):
    num = int(input())

    #왼쪽부터 넣기
    if len(left_heap) == len(right_heap):
        heapq.heappush(left_heap, (-num, num))
    else:
        heapq.heappush(right_heap, (num, num))
    
    #조건 비교
    if right_heap and left_heap[0][1] > right_heap[0][1]:
        left = heapq.heappop(left_heap)[1]
        right = heapq.heappop(right_heap)[1]

        heapq.heappush(left_heap, (-right, right))
        heapq.heappush(right_heap, (left, left))
    
    #출력
    print(left_heap[0][1])


    
    

    
    

