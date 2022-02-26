#수 정렬하기2 

#합병 정렬
def mergemerge(arr):
    if len(arr) <= 1:
        print("1자리수인 예외 경우 arr",arr)
        return arr
    
    mid = len(arr)//2
    mrg = []
    print("merge함수 시작",arr)
    print("arr[:mid ",arr[:mid],"arr[mid:]",arr[mid:])
    left, right = mergemerge(arr[:mid]),mergemerge(arr[mid:])
    
    print("--",left,right)
    i,j = 0,0
    k =0
    while i < len(left) and j < len(right):
        print("while문 시작")
        k += 1
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
    print("while문 횟수,i,j",k,i,j)
    if i != len(left):
        print("if 문의 i {0} != len(left) {1}".format(i,len(left)))
        print(left[i:])
        mrg += left[i:]
        print("mrg:"+str(mrg[:]))
    if j != len(right):
        print("if 문의 j {0} != len(left) {1}".format(j,len(right)))
        mrg += right[j:]
        print("mrg:"+str(mrg[:]))
    
    print(mrg)
    print("left,right",left,right)
    print("mrg return")
    return mrg 

N = int(input())

arr =[]
for i in range(N):
    arr.append(int(input()))

answer = mergemerge(arr)
print("answer: ",answer)

