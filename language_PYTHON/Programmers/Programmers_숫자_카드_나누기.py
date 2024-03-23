
def gcd(x, y):
    while y:
        x, y = y, x%y

    return x


def solution(arrayA, arrayB):
    answer = 0
    # min = 2
    gcd_A = arrayA[0]

    for index, val in enumerate(arrayA):
        if index == 0: continue

        gcd_A = gcd(gcd_A, val)
    
    flag_A = True
    for val in arrayB:
        if val % gcd_A == 0:
            flag_A = False
            break
    
    if flag_A:
        answer = max(answer, gcd_A)


    gcd_B = arrayB[0]

    for index, val in enumerate(arrayB):
        if index == 0: continue

        gcd_B = gcd(gcd_B, val)

    flag_B = True
    for val in arrayA:
        if val % gcd_B == 0:
            flag_B = False
            break

    if flag_B:
        answer = max(answer, gcd_B)
        
    return answer


solution([14, 35, 119], [18, 30, 102])