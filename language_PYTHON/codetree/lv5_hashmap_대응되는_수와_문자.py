import sys
si = sys.stdin.readline
N, M = map(int, si().split())
di = dict()

array_num = [si().strip() for i in range(N)]
for i in range(len(array_num)):
    string = array_num[i]
    di[string] = i+1


for i in range(M):
    input = si().strip()
    if(input.isalpha()):
        print(di[input])
    else: # 숫자일 때
        print(array_num[int(input)-1])