#곱셈
A,B,C = map(int,input().split())

def dac(A,B,C):
    if B ==1:
        return A % C
    
    if B % 2 == 0:
        print("b%2")
        return (dac(A,B//2,C)**2)%C
    else:
        print("b%2 != 0")
        return ((dac(A,B//2,C)**2)*A)%C
print(dac(A,B,C))