#수 정렬하기
#시간복잡도 O(n**2)인 버블정렬,삽입정렬 등으로 풀어보자


N = int(input())
numbers = []
for i in range(N):
    numbers.append(int(input()))


def insert_sort(x):
    for i in range(1,len(x)):
        j = i-1
        key = x[i]
        while x[j] > key and j >= 0:
            x[j+1]=x[j]
            j = j-1
            x[j+1] = key
    return x
numbers = insert_sort(numbers)
for i in numbers:
    print(i)