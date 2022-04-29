# 시험감독 - 삼성 기출

# B >= 1 C 는 상관없음
N = int(input())
tester_array = list(map(int, input().split()))
main, sub = map(int,input().split())

answer = []
for tester in tester_array:
    cnt = 0
    if tester <= main:
        cnt += 1
        answer.append(cnt)

    else: # 값이 tester가 더 커서 sub를 추가해야하는 경우
        cnt += 1 # main 으로 1차 
        left_tester = tester - main

        if left_tester % sub == 0: # 딱맞아 떨어지면 그대로
            a = left_tester // sub # 몫
            cnt = cnt + a
        else:
            a = left_tester // sub # 몫
            cnt = cnt + a + 1 # 하나 더 필요하므로
        answer.append(cnt)
         
            
print(sum(answer))


