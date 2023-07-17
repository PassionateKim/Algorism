# 복습 횟수:0, 00:30:00, 복습필요:X
import sys
si = sys.stdin.readline

while(1):
    answer = 0

    data = si().rstrip()
    if not data:
        break
    N, M = map(int, data.split())
    for target_num in range(N, M+1):
        target_str = str(target_num)
        target_set = set(target_str)

        if(len(target_str) == len(target_set)):
            answer += 1
    
    print(answer)
