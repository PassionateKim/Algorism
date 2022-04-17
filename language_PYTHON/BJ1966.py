#프린터 큐
import sys
for i in range(int(input())):
    N,M = map(int,sys.stdin.readline().split())
    print_list = list(map(int,sys.stdin.readline().split()))
    idx =[0 for _ in range(N)]
    idx[M] = 1

    cnt = 0
    while True:
        print(print_list)
        if print_list[0] == max(print_list):
            cnt += 1
            if idx[0] == 1:
                print(cnt)
                break
            else:
                print_list.pop(0)
                idx.pop(0)
        else:
            print_list.append(print_list.pop(0))
            idx.append(idx.pop(0))
            

