# 에디터
import sys
from collections import deque
si = sys.stdin.readline

str_left = deque(map(str,si().strip()))
str_right = deque()
N = int(si())

for i in range(N):
    input = si().strip() 
    # 커서를 왼쪽으로 한 칸 옮김 (커서가 문장의 맨 앞이면 무시됨)
    if input == 'L':
        if str_left:
            str_right.appendleft(str_left.pop())
    # 커서를 오른쪽으로 한 칸 옮김 (커서가 문장의 맨 뒤이면 무시됨)
    if input == 'D':
        if str_right:
            str_left.append(str_right.popleft())
    # 커서 왼쪽에 있는 문자를 삭제함 (커서가 문장의 맨 앞이면 무시됨)
    if input == 'B':
           if str_left:
            str_left.pop()
    # $라는 문자를 커서 왼쪽에 추가함
    if 'P' in input:
        print(input.split())
        str_left.append(input.split()[1])

str_left.extend(str_right)
for i in str_left:
    print(i,end="")