import sys
si = sys.stdin.readline
n = int(si())
a = sorted(list(map(int, si().split())))

best_sum = 1<<32

def lower_bound(array, start, end, target): 
    res = end
    while start<=end:
        mid = (start + end) // 2
        if array[mid] >= target:
            res = mid
            end = mid - 1
        else:
            start = mid + 1 
    return res

v1, v2 = 0, 0
for l in range(len(a)-1):
    candidate = lower_bound(a, l+1, len(a)-1, -a[l])

    if abs(a[l] + a[candidate]) < best_sum:
        best_sum = abs(a[l] + a[candidate])
        v1, v2 = a[l], a[candidate]
    
    if l < candidate-1 and abs(a[l] + a[candidate-1]) < best_sum:
        best_sum = abs(a[l] + a[candidate-1])
        v1, v2 = a[l], a[candidate-1]
    
print(v1, v2)
