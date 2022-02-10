#피보나치 수 5

F = [0,1]

#1~18까지 for문 돌리기 
for i in range(19):
    F.append(F[i]+F[i+1])


n = int(input())
print(F[n])