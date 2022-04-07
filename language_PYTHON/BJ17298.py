#오큰수
from inspect import stack
from turtle import st


N = int(input())
arr = list(map(int,input().split()))
answer = [-1] * N
stack = [0]

for i in range(N):
    while stack and arr[stack[-1]] < arr[i]:
        answer[stack.pop()] = arr[i]
    
    stack.append(i)
print(answer)