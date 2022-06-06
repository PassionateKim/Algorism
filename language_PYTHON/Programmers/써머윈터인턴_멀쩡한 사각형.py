# 멀쩡한 사각형

def gcd(a, b): # 최대공약수 구하기 - 유클리드 호제법
    while b:
        a, b = b, a % b
    return a


def solution(w, h):
    x = gcd(w, h)
    return w * h - (w//x + h//x - 1)*x