#회전하는 큐
# 복습 횟수:3, 00:45:00, 복습필요X
import sys
from collections import deque
si = sys.stdin.readline 
N, M = map(int, si().split())

pick_list = list(map(int, si().split()))
original_list = deque([i for i in range(1, N + 1)])
answer = 0


for target in pick_list:
    target_index = original_list.index(target)

    
    left = 0
    right = len(original_list) - 1
    mid = (left + right) // 2

    if len(original_list) % 2 == 0: # 짝수인 경우
        if target_index <= mid + 1: # 왼쪽에서 뺀다.
            while True:
                if original_list[0] == target:
                    original_list.popleft()
                    break

                val = original_list.popleft()
                answer += 1
                original_list.append(val)
                
        else:
            while True:
                if original_list[0] == target:
                    original_list.popleft()
                    break

                val = original_list.pop()
                answer += 1
                original_list.appendleft(val)
    else:
        if target_index <= mid: # 왼쪽에서 뺀다.
            while True:
                if original_list[0] == target:
                    original_list.popleft()
                    break

                val = original_list.popleft()
                answer += 1
                original_list.append(val)
                
        else:
            while True:
                if original_list[0] == target:
                    original_list.popleft()
                    break

                val = original_list.pop()
                answer += 1
                original_list.appendleft(val)

print(answer)