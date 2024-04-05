import sys
si = sys.stdin.readline 

arr = list(map(str, si().rstrip()))

left_count = 0
right_count = 0
total_sum = 0
answer = 0

for i in range(len(arr)):
    # init 초기화
    if arr[i] == '(':
        left_count += 1
        total_sum += 1 
    else:
        right_count += 1
        total_sum -= 1
    
    # 올바른 괄호가 되기 위해선 누적합이 >= 0 이어야 한다. 
    # 만약 -1이 된다면 그 때까지의 ')' 개수가 가능한 오타의 개수이다.
    if total_sum == -1:
        answer = right_count
        break
    
    # total = 1 일 때, ')'를 '('로 바꾸면 '('가 더 많은 경우로 (())) 이런 꼴이 되어버려 올바른 기호 즉, total >= 0 조건을 만족하지 못하므로
    # 변경해야 할 '(' 괄호는 없다.
    if total_sum == 1:
        left_count = 0 

# 만약 '('가 더 많은 경우 초기화 이후의 모든 left_count 값은 오타가 될 수 있다.
if total_sum == 2:
    answer = left_count

print(answer)