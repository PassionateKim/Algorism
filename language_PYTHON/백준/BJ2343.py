# 기타레슨
import sys
si = sys.stdin.readline
n, m = list(map(int, si().split()))
a = list(map(int, si().split()))

def determination(array, size, target_num):
    sum = 0
    cnt = 1
    for video in array:
        sum += video
        if sum > size: # 사이즈를 넘는 경우
            sum = video
            cnt += 1
        else:
            pass
    return cnt <= target_num




def Binary(array, start, end, target):
    ans = 0
    while start<=end:
        mid = (start+end)//2
        if determination(array, mid, target):
            ans = mid
            end = mid - 1
        else:
            start = mid + 1

    return ans

print(Binary(a, max(a), int(1e7), m))







# # len 은 무엇을 의미하는지 고민해보기 
# # l이 1이 아닌 max(a)가 되어야하는 이유 다시 생각해보기
# # ans = 28 이어서 cnt 2가 되는 경우 조합이 2개인데 왜 조건을 만족하는 것으로 설계 했는지
# def determination(len):
#     cnt, sum = 1, 0
#     for x in a:
#         if sum + x > len:
#             cnt += 1
#             sum = x
#         else:
#             sum += x
#     return cnt <= m

# l, r, ans = max(a), 1000000000, 0
# while l <= r:
#     mid = (l + r) // 2
#     if determination(mid):
#         ans = mid
#         r = mid - 1
#     else:
#         l = mid + 1

# print(ans)