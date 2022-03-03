#좌표압축

#직선 위에 N개의 좌표 X1, X2, ..., XN이 있다. 이 좌표에 좌표 압축을 적용하려고 한다.
#Xi를 좌표 압축한 결과 X'i의 값은 Xi > Xj를 만족하는 서로 다른 좌표의 개수와 같아야 한다.
#X1, X2, ..., XN에 좌표 압축을 적용한 결과 X'1, X'2, ..., X'N를 출력해보자.
import sys
#1. 정의
N = int(input())
xArray = []
setArray = []
answerArray = []
#2. 입력값넣기
xArray = list(map(int,sys.stdin.readline().rstrip().split()))

#3. 비즈니스로직 -> 비교해서 array에 넣기
#3-1 setArray를 set으로 중복 삭제하기
setArray = set(xArray)
setArray = list(setArray)

#3-2 비교해서 값에 넣기
for i in range(len(xArray)):
    press = 0
    for j in range(len(setArray)):
        if(xArray[i] > setArray[j]):
            press += 1
    answerArray.append(press)

for answer in answerArray:
    print(answer,end=" ")
    

