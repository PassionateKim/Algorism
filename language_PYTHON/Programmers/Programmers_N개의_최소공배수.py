
def GCD(start, end):
    while end:
        start, end = end, start % end
    
    return start


def LCM(start, end):
    start_list = []

    while True:
        gcd = GCD(start, end)
        if gcd == 1:
            start_list.append(start)
            start_list.append(end)
            
            return_val = 1
            for val in start_list:
                return_val *= val
                
            return return_val

        start_list.append(gcd)
        start = start // gcd
        end = end // gcd
        

def solution(arr):
    start = arr[0]

    
    for index in range(1, len(arr)):
        start = LCM(start, arr[index])
        
    return start


solution([2,6,8,14])