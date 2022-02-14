#별 찍기 - 10

def count_star(a : list):
    unDeterminedStar = []
    for i in range(3*len(a)):
        if(i//len(a) == 1):
            unDeterminedStar.append(a[i%len(a)]+" "*len(a)+a[i%len(a)])
        else:
            unDeterminedStar.append(a[i%len(a)]*3)
    return unDeterminedStar



#3일 때 
star = ["***","* *","***"]

N = int(input())
T = 0
while N != 3:
    N = N//3
    T += 1

#T값을 통해 재귀함수를 몇번 돌릴지 체크해준다. 9 ->  1 번 27 -> 2번 81 -> 3번
for i in range(T):
    star = count_star(star)


for i in star:
    print(i)




    