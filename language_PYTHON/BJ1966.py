#프린터 큐
import sys
for i in range(int(input())):
    N,M = map(int,sys.stdin.readline().split())
    print_list = list(map(int,sys.stdin.readline().split()))
    idx = [0 for i in range(N)]
    idx[M] = 1 # 궁금한 문서위치 저장하기
    
    #제일 큰것인지 아닌지를 체크하고 
    #큰 것이면 빼고 아니면 뒤로
    #standard 가 아닌 것을 빼면 cnt += 1
    cnt = 0
    while True:
        print("print_list:",print_list)
        if print_list[0] == max(print_list):
            cnt += 1
            # 같은 값인 경우 위치
            if idx[0] == 1:
                print(cnt)
                break
            else:
                print_list.pop(0)
                idx.pop(0)

        else:
            print_list.append(print_list.pop(0))
            idx.append(idx.pop(0))


            
