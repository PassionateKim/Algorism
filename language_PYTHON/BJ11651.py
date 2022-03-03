#좌표 정렬하기 2
#2차원 평면 위의 점 N개가 주어진다. 좌표를 y좌표가 증가하는 순으로,
#  y좌표가 같으면 x좌표가 증가하는 순서로 정렬한 다음 출력하는 프로그램을 작성하시오.

from array import array
import sys

N = int(input())
xy_arrays = []
#1. 값넣기
for i in range(N):
    xy_arrays.append(list(map(int,sys.stdin.readline().split())))

xy_arrays.sort(key= lambda x: (x[1],x[0]))

for i in xy_arrays:
    print(i[0],i[1])