# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
from collections import deque
def solution(N):
    # Implement your solution here
    array = deque()
    while(N != 0):
        val = N % 2
        N = N // 2

        array.appendleft(val)
        
    answer = 0
    flag = 0
    tmp = 0
    for i in range(len(array)):
        if flag == 0 and (array[i] == 1):
            flag = 1

        elif flag == 1 and (array[i] == 1):
            answer = max(answer, tmp)
            tmp = 0
            
        elif flag == 1 and (array[i] == 0):
            tmp += 1
        

N = int(input())
solution(N)