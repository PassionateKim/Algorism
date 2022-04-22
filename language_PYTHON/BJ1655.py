#가운데를 말해요
import sys
import heapq
input = sys.stdin.readline

N = int(input())
left_heap = []
right_heap = []

for i in range(N):
    s = int(input())
    
    #왼쪽힙부터 오른쪽 순차적으로 값을 넣어보기
    if len(left_heap) == len(right_heap):
        heapq.heappush(left_heap,(-s, s))
    else:
        heapq.heappush(right_heap,(s, s))
    #비교해서 넣기
    if i > 0 and left_heap[0][1] > right_heap[0][1]:
        #동시에 빼기
        left = heapq.heappop(left_heap)[1]
        right = heapq.heappop(right_heap)[1]

        heapq.heappush(left_heap, (-right, right)) 
        heapq.heappush(left_heap, (-left, left))
    
    #출력
    print(left_heap[0][1])
    

    
    

