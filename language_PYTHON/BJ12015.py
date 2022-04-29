# 가장 긴 증가하는 부분 수열 2
N = int(input())
A = list(map(int,input().split()))

LIS = [0]
arr = [0] + A

for item in arr:
    if LIS[-1] < item:
        LIS.append(item)
    else:
        start = 0
        end = len(LIS)
        while start <= end:
            mid = (start + end) // 2

            if LIS[mid] < item: # 작으면 절대 안되니까.
                start = mid + 1  
            else:
                end = mid - 1
        LIS[start] = item

print(LIS)

# 가장 긴 증가하는 부분 수열 2
# N = int(input())
# A = list(map(int,input().split()))

# LIS = [0]
# A_array = [0] +  A

# for item in A_array:
#     if LIS[-1] < item:
#         LIS.append(item)
#     else: # LIS 의 원소들을 비교해서 그 안에 값을 넣어주어야한다.
#         start = 0
#         end = len(LIS) - 1
        
#         while start <= end:
#             mid = (start + end) // 2

#             if LIS[mid] < item:
#                 start = mid + 1
#             else:
#                 end = mid - 1
#         LIS[start] = item

# print(LIS)





