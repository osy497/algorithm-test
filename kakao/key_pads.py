#!/bin/python3

def conv(cur):
    if cur == '*':
        cur_x = 0
        cur_y = 0
    elif cur == '#':
        cur_x = 2
        cur_y = 0
    elif cur == '0':
        cur_x = 1
        cur_y = 0
    else:
        cur_x = (int(cur) -1) % 3
        cur_y = 3 - (int(cur) -1 ) // 3
    return [cur_x, cur_y]

def dist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])



def solution(numbers, hand):
    answer = ''
    cur_l = '*'
    cur_r = '#'
    LEFT = ['1', '4', '7']
    RIGHT = ['3', '6', '9']
    for e in numbers:
        if str(e) in LEFT:
            answer += 'L'
            cur_l = str(e)
        elif str(e) in RIGHT:
            answer += 'R'
            cur_r = str(e)
        else:
            l_dist = dist(conv(cur_l), conv(str(e)))
            r_dist = dist(conv(cur_r), conv(str(e)))
            if l_dist < r_dist:
                answer += 'L'
                cur_l = str(e)
            elif l_dist > r_dist:
                answer += 'R'
                cur_r = str(e)
            else:

                if hand == "right":
                    answer += "R"
                    cur_r = str(e)
                elif hand == "left":
                    answer += "L"
                    cur_l = str(e)


    return answer
print(solution([], "right"))
#print(dist(conv('#'), conv('0')), dist(conv('0'), conv('7')))

