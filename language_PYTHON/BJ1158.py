# 요세푸스 문제
from collections import deque

N, K = map(int, input().split())

table = deque()
answer = []

for i in range(1, N+1):
    table.append(i)

while table:

    for i in range(K-1): # K -1 번만큼 반복한다
        table.append(table.popleft())
    
    answer.append(table.popleft())

print("<",end='')
print(", ".join(map(str, answer)),end='')
print(">")    