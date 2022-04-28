# 가장 긴 증가하는 부분 수열 2
N = int(input())
A = list(map(int,input().split()))

LIS = [0]
arr = [0] + A
for item in arr:  
    if LIS[-1] < item:
        LIS.append(item)

    else:
        left = 0
        right = len(LIS)
        while left < right:
            mid = (left + right) // 2
            
            if LIS[mid] < item:
                left = mid + 1
            else:
                right = mid

        LIS[right] = item

print(len(LIS) - 1)


    


    

