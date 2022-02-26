#수 정렬하기
#시간복잡도 O(n**2)인 버블정렬,삽입정렬 등으로 풀어보자


N = int(input())
numbers = []
for i in range(N):
    numbers.append(int(input()))


def bubble_sort(x):
    length = len(x)-1
    for i in range(length):
        for j in range(length-i):
            if (x[j] > x[j+1]):
                x[j],x[j+1] = x[j+1],x[j]
    return x

    
numbers = bubble_sort(numbers)
for i in numbers:
    print(i)

