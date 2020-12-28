#!/bin/python3


import copy

def solution(s):
    answer = 0
    s_list = list(s)

    m = len(s_list)

    for length in range(1, len(s_list)//2 + 1):
        tmp = []
        tmp_s = copy.deepcopy(s_list)
        for _ in range(len(s_list)//length):
            tmp.append(''.join(tmp_s[:length]))
            tmp_s = tmp_s[length:]

        if tmp_s:
            tmp.append(tmp_s)

        pivot = ""
        amount = 0
        tmp_result = ""
        for e in tmp:
            if pivot:
                if e == pivot:
                    amount += 1
                else:
                    if amount == 1:
                        tmp_result += str(pivot)
                    else:
                        tmp_result += str(amount)+str(pivot)
                    pivot=''.join(e)
                    
                    amount = 1
                    
            else:
                pivot = ''.join(e)
                amount = 1

        if amount == 1:
            tmp_result += str(pivot)
        else:
            tmp_result += str(amount)+str(pivot)
        print(tmp_result)

        m = min(m, len(tmp_result))
            

    return m

s = "ababcdcdababcdcd"
print(solution(s))
