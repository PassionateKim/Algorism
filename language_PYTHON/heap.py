import sys

#힙 구현
def heapify(array):
    for i in range(len(array)//2 -1,-1,-1):
        parent = i

        while parent <= len(array) // 2:
            child = parent * 2 + 1
            if child + 1 < len(array) and array[child] < array[child + 1]:
                child += 1

            if array[parent] < array[child]:
                tmp = array[child]
                array[child] = array[parent]
                array[parent] = tmp
            parent = child
            print(array) 

    
    # #자식이 있는 부모 노드만 체크하는 것이므로 len(array) // 2 로 시작한다.
    # for i in range(len(array)//2 - 1,-1,-1):
    #     parent = i
    #     #자식이 있을 조건
    #     while parent < len(array) // 2:
    #         print("parent index",parent)
    #         child = parent * 2 + 1
    #         print("child index", child)
    #         #값이 큰 자식을 기준으로 하기 위한 if문 -> 이해 안되면 반대를 생각해보기
    #         if child + 1 < len(array) and array[child + 1] > array[child]:
    #             child += 1
    #         #자식노드와 비교
    #         if array[parent] < array[child]:
    #             tmp = array[child]
    #             array[child] = array[parent]
    #             array[parent] = tmp
    #         parent = child
    #         print(array)

def heappop(array):
    if not array:
        return 0
    elif len(array) == 1:
        return array.pop()

    value = array[0]
    array[0] = array.pop()
    parent = 0

    while True:
        child = parent * 2 + 1
        #print(child)
        if child >= len(array):
            break
        
        if child + 1 < len(array) and array[child + 1] > array[child]:
            child += 1

        if array[parent] < array[child]:
            tmp = array[child]
            array[child] = array[parent]
            array[parent] = tmp

        parent = child
    return value

def heappush(array,value):
    array.append(value)
    now = len(array) - 1

    while now > 0:
        parent = (now-1) // 2

        if array[now] > array[parent]:
            tmp = array[now]
            array[now] = array[parent]
            array[parent] = tmp
        now = parent

input = sys.stdin.readline

# n = int(input())

array = [1,2,3,4,5,6,7,8,9,10]

heapify(array)

# for i in range(n):
#     order = int(input())
#     if order == 0:
#         print(heappop(array))
#     else:
#         heappush(array,order)