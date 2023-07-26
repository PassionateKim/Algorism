# 전구와 스위치
# 복습 횟수:1, 00:45:00, 복습필요X
import sys
si = sys.stdin.readline 

N = int(si())
current_state = list(map(int, si().rstrip()))
hope_state = list(map(int, si().rstrip()))

def converter(index, coped_state):
    if coped_state[index] == 1:
       coped_state[index] = 0
    else:
        coped_state[index] = 1
# 맨 앞과 맨 끝만 차이가 있다. 
# 맨 처음을 누른 경우 
answer = []


def on_off(candidate):
    for i in range(1, len(coped_state)):
        if i == len(coped_state) -1: # 마지막 인덱스인 경우
            if coped_state[i-1] != hope_state[i-1]:
                candidate += 1
                converter(i-1, coped_state)
                converter(i, coped_state)
        else:
            if coped_state[i-1] != hope_state[i-1]:
                candidate += 1
                converter(i-1, coped_state)
                converter(i, coped_state)
                converter(i+1, coped_state)
    return candidate

coped_state = current_state[:]
candidate1 = 1
converter(0, coped_state)
converter(1, coped_state)
candidate1 = on_off(candidate1)
if coped_state == hope_state:
    answer.append(candidate1)

# 맨 처음을 누르지 않은 경우

candidate2 = 0
coped_state = current_state[:]

candidate2 = on_off(candidate2)
if coped_state == hope_state:
    answer.append(candidate2)

if len(answer) == 0:
    print(-1)
else:
    print(min(answer))