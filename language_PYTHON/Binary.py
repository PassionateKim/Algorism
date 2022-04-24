# 이분탐색

array = [4,3,5,1,2,6] # 정렬되지 않은 배열
array = sorted(array) # sorted 로 정렬하기 
print("array:",array)

def binary_search(array, target, start, end):
    if start > end: # 탐색이 끝났음에도 값을 찾지 못한 경우
        return None
    mid = (start + end) // 2
    print(array[mid])
    # 원하는 값 찾은 경우 값을 반환
    if array[mid] == target:
        return array[mid]
    # 원하는 값이 중간 값보다 작은 경우 왼쪽부분 확인
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    # 원하는 값이 중간 값보다 큰 경우 오른쪽부분 확인
    else:
        return binary_search(array, target, mid + 1, end)

result = binary_search(array, 2, 0, len(array) -1)

if result is None:
    print("원소가 존재하지 않습니다.")
else:
    print("원소는 "+str(result)+"입니다.")

