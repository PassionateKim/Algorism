# 위험한 효도
a, b, d = map(int, input().split())
differ = d
sum = 0

# 술래에게 다가가는 경우
while True:
    differ = differ - a #a 초간 뒤를 보고 있음
    sum += a # a초간 간만큼의 시간 더하기
    if differ <= 0: # 터치하는 경우
        x = abs(0 - differ) # 오버한 만큼 다시 빼기
        sum -= x
        break
    sum += b # b초간 대기 시간 더하기

# 술래에게서 멀어지는 경우
differ2 = d # distance 초기화

while True:
    differ2 = differ2 - b #b 초간 뒤를 보고 있음
    sum += b #b초간 간만큼의 시간 더하기
    if differ2 <= 0: #도착하는 경우
        x = abs(0 - differ2) # 오버한 만큼 다시 빼기
        sum -= x
        break
    sum += a # a초간 대기 시간 더하기



print(sum)

