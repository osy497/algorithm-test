#!/bin/python3
def check_right(p):
    l_paren = 0
    r_paren = 0
    i = 0
    p_list = list(p)
    while i < len(p_list):
        if p_list[i] == "(":
            l_paren += 1
        else:
            r_paren += 1
        if r_paren > l_paren:
            return False
        i+=1

    return True
def split(p):
    l_paren = 0
    r_paren = 0
    i = 0
    u = ""
    v = p

    p_list = list(p)

    for i in range(len(p_list)):
        if  p_list[i] == "(":
            l_paren += 1
        elif p_list[i] == ")":
            r_paren += 1
        if r_paren == l_paren:
            u += v[:i+1]
            v = v[i+1:]
            break

    return ''.join(u), ''.join(v)

def fourth(u, v):
    tmp_v = "(" + __solution(v) + ")"
    tmp_u = ""
    for e in list(u[1:len(u)-1]):
        if e == "(":
            tmp_u += ")"
        else:
            tmp_u += "("
    return tmp_v + tmp_u
def __solution(p):
    if p == "":
        return ""
    u, v = split(p)
    if check_right(u):
        return u + __solution(v)
    else:
        return fourth(u, v)

def solution(p):
    answer = ''
    answer = __solution(p)

    return answer
print(solution("(()())()"))
