from array import array
from lib2to3.pgen2.token import RIGHTSHIFT
from re import A
from tkinter import ARC


def merge_sort(array):
    if len(array) <= 1:
        return array

    mid = len(array) //2    
    print(array[:mid],array[mid:])
    left, right = merge_sort(array[:mid]),merge_sort(array[mid:])
    print("left:"+str(left),"right:"+str(right),"mid:"+str(mid))
    i,j,k = 0,0,0
    
    
    while i < len(left) and j < len(right):
        if left[i] <right[j]:
            array[k] =left[i]
            i += 1
        else:
            array[k] = right[j]
            j +=1
        k += 1
    print("i:",i,"j:",j)
    if i == len(left): #한쪽 리스트가 끝난 경우, 나머지 리스트를 넣어줌
        print("--i = len(left")
        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1
    elif j == len(right):
        print("--j = len(right)")
        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1
    print("return! array:",array)
    return array

n = int(input())
array = []

for _ in range(n):
    array.append(int(input()))

array = merge_sort(array)

for data in array:
    print(data)