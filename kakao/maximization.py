#!/bin/python3
import copy

def pick(expression):
    result = set()
    CHECK = "+-*"
    tmp = list(expression)
    for e in tmp:
        if e in CHECK:
            result.add(e)

    return list(result)



sub = []
def foo(operator, l):
    global sub
    if not operator:
        sub.append(l)
        return

    for i in range(len(operator)):
        tmp = copy.deepcopy(l)
        tmp_op = copy.deepcopy(operator)
        tmp.append(tmp_op[i])
        del tmp_op[i]
        foo(tmp_op, tmp)


def bar(expression, op):

    CHECK = "*-+"
    tmp_op = []
    tmp_num = []
    tmp = ""
    for e in expression:
        if e in CHECK:
            tmp_op.append(e)
            tmp_num.append(int(tmp))
            tmp = ""
        else:
            tmp += e
    tmp_num.append(int(tmp))


    while op:
        i = 0
        while i < len(tmp_op):
            if tmp_op[i] == op[0]:
                if tmp_op[i] == "+":
                    tmp_num[i] = tmp_num[i] + tmp_num[i+1]
                elif tmp_op[i] == "-":
                    tmp_num[i] = tmp_num[i] - tmp_num[i+1]
                elif tmp_op[i] == "*":
                    tmp_num[i] = tmp_num[i] * tmp_num[i+1]
                del tmp_num[i+1]
                del tmp_op[i]
            else:
                i += 1
        del op[0] 

    return tmp_num[0]
            


            


def solution(expression):
    answer = 0
    inp = pick(expression)
    foo(inp, [])

    for e in sub:
        answer = max(answer, abs(bar(expression, e)))


    print(answer)

    return answer


#solution("50*6-3*2")
solution("100")
