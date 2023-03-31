# 히스토그램
# 복습 횟수:0, 02:00:00, 복습필요O
import sys
si = sys.stdin.readline

N = int(si())
height_list = []

for i in range(N):
    height = int(si())
    height_list.append(height)

stack = []
candidate = []
# stack을 활용하기 
for idx in range(len(height_list)):
    if idx == 0:
        stack.append([idx, height_list[0]])
    else:
        if stack[-1][1] <= height_list[idx]:
            stack.append([idx, height_list[idx]])
        else: # stack[-1] > height_list[idx]
            while stack:
                if stack[-1][1] > height_list[idx]:
                    i, height = stack.pop()
                    if not stack: # 비는 경우
                        width = idx
                    else:
                        before_idx = stack[-1][0]
                        width = idx - before_idx - 1

                    candidate.append(width * height)        
                else:
                    break
            
            stack.append([idx, height_list[idx]])

while stack:
    i, height = stack.pop()
    if not stack:
        width = N
    else:
        before_idx = stack[-1][0]
        width = N - before_idx - 1

    candidate.append(width * height)

print(max(candidate))