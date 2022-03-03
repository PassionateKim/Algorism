#좌표 정렬하기


from re import X
import sys
N = int(input())
xy_array=[]
for i in range(N):
    xy_array.append(list(map(int,sys.stdin.readline().split())))

xy_array.sort()
#for 문으로???

for i in range(N):
    print(xy_array[i][0],xy_array[i][1])