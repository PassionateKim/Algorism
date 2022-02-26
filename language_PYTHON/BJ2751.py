#수 정렬하기2 

#합병 정렬

def mergemerge(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr)//2
    mrg = []
    print("arr[:mid ",arr[:mid],"arr[mid:]",arr[mid:])
    left, right = mergemerge(arr[:mid]),mergemerge(arr[mid:])
    print("--",left,right)
    i,j = 0,0
    while i < len(left) and j < len(right):
        if left[i] <right[j]:
            print("** left {0} < right {1}이므로 ".format(i,j))
            mrg.append(left[i])
            print("mrg:"+str(mrg[:]))
            i += 1
        else:
            print("** left {0} >= right {1}이므로 ".format(i,j))
            mrg.append(right[j])
            print("mrg:"+str(mrg[:]))
            j += 1
    if i != len(left):
        print("## {0} != "+str(len(left))+"이므로".format(i))
        mrg += left[i:]
        print("mrg:"+str(mrg[:]))
    if j != len(right):
        print("## {0} != "+str(len(right))+"이므로".format(j))
        mrg += right[j:]
        print("mrg:"+str(mrg[:]))
    print("mrg return")
    return mrg




N = int(input())

arr =[]
for i in range(N):
    arr.append(int(input()))

answer = mergemerge(arr)
for n in answer:
    print(n)

