# 키패드 누르기
def solution(numbers, hand):
    result = []
    left_hand, right_hand = "*", "#"
    locations = dict()
    locations["1"] = (0,0)
    locations["2"] = (0,1)
    locations["3"] = (0,2)
    locations["4"] = (1,0)
    locations["5"] = (1,1)
    locations["6"] = (1,2)
    locations["7"] = (2,0)
    locations["8"] = (2,1)
    locations["9"] = (2,2)
    locations["*"] = (3,0)
    locations["0"] = (3,1)
    locations["#"] = (3,2)
    
    for num in numbers:
        if str(num) in "147":
            result.append('L')
            left_hand = str(num)
        elif str(num) in "369":
            result.append('R')
            right_hand = str(num)
        else:
            # 두 엄지손가락의 현재 키패드 위치에서 더 가까운 엄지손가락 사용
            will_xy, left_xy, right_xy = locations[str(num)], locations[left_hand], locations[right_hand]
            left_differ = abs(left_xy[0] - will_xy[0]) + abs(left_xy[1] - will_xy[1])
            right_differ = abs(right_xy[0] - will_xy[0]) + abs(right_xy[1] - will_xy[1])
            if left_differ < right_differ:
                result.append('L')
                left_hand = str(num)
            elif left_differ > right_differ:
                result.append('R')
                right_hand = str(num)
            else:
                if hand == "left":
                    result.append('L')
                    left_hand = str(num)
                else:
                    result.append('R')
                    right_hand = str(num)
    a = "".join(result)
    print(a)
    return

solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right")
      
    
    
    
    
    

