# 귀여운 라이언
# 복습 횟수:2, 00:30:00, 복습필요X
import sys
si = sys.stdin.readline 

N, K = map(int, si().split())
arr = list(map(int, si().split()))

result = int(1e9)
count = 0

left = 0
right = 0

one = 0
answer = sys.maxsize

if arr[left] == 1:
    one += 1

while left < len(arr) and right < len(arr):
    # 라이언 인형의 개수가 부족하면 오른쪽으로 포인터
    if one < K:
        right += 1
        if right < len(arr) and arr[right] == 1:
            one += 1
    
    else:
        if one == K:
            answer = min(answer, right - left + 1)
        
        if left < len(arr) and arr[left] == 1:
            one -= 1
        
        left += 1

if answer == sys.maxsize:
    print(-1)
else:
    print(answer)