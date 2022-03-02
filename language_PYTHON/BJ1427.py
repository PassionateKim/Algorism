#소트인사이드

#문제
#배열을 정렬하는 것은 쉽다. 수가 주어지면, 그 수의 각 자리수를 내림차순으로 정렬해보자.
import sys
from tkinter.tix import Tree
# check_num = list(map(int,str(a)))
num_array = list(map(int,str(input())))
num_array.sort(reverse=True)

for _ in num_array:
    print(_,end='')