# 반지
import sys
si = sys.stdin.readline
string = list(map(str, si().rstrip()))
N = int(si())
answer = 0
for i in range(N):
    ring = list(map(str, si().rstrip()))
    # 시작과 끝이 연결되어있으므로 그냥 ring + ring 해서 완전탐색한다.
    ring = ring + ring
    
    for i in range(len(ring)-len(string)):
        flag = 1
        for j in range(len(string)):
            if (string[j] != ring[i+j]):
                flag = 0
                break
        
        if flag:
            answer += 1
            break

print(answer)