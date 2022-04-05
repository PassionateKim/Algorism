#균형잡힌 세상
from collections import deque
import sys

while True:
    char_list = deque()
    s = sys.stdin.readline().rstrip()
    if s == ".":
        break
    temp = True
    for i in s:
        if i == "(" or i == "[":
            char_list.append(i)
        elif(i == ")"):
            if(len(char_list) == 0 or char_list[-1] != "("):
                temp = False
                break
            else:
                char_list.pop()    
        elif(i == "]"):
            if(len(char_list) == 0 or char_list[-1] != "["):
                temp = False
                break
            else:
                char_list.pop()
    print(char_list)
    #char 에 값이 들어있는데 temp 가 True 인 경우 가 반례??...
    if temp == True :
        print('yes')
    else:
        print('no')
   
