#!/bin/python3
import copy

def solution(n, m, board):
    tmp_map = [list(x) for x in board]
    exist = [[False] * n for _ in range(m)]
    cand = [[False] * n for _ in range(m)]

    tm = [["O"] * n for _ in range(m)]


    for i in range(n):
        for j in range(m):
            tm[j][n - i -1] = tmp_map[i][j]

    #start remove
    while True:
        tmp_cand = copy.deepcopy(cand)
        tmp_exist = copy.deepcopy(exist)

        ii = 0
        jj = 0
        for e1 in tm:
            for e2 in e1:
                tmp_exist[ii][jj] = True
                jj += 1
            ii += 1
            jj = 0



        for i in range(m - 1):
            for j in range(n - 1):
                if tmp_exist[i][j] and tmp_exist[i+1][j] and tmp_exist[i][j+1] and tmp_exist[i+1][j+1]:
                    tmp = tm[i][j]
                    if tmp == tm[i+1][j] and tmp == tm[i][j+1] and tmp == tm[i+1][j+1]:
                        tmp_cand[i][j] = True
                        tmp_cand[i+1][j] = True
                        tmp_cand[i][j+1] = True
                        tmp_cand[i+1][j+1] = True
        for i in range(m):
            for j in range(n):
                if tmp_cand[i][n-j-1] == True:
                    del tm[i][n-j-1]
        cont = 0
        for e in tmp_cand:
            if True in e:
                cont = 1
        if cont == 0:
            break

    result = 0
    for e1 in tm:
        for e2 in e1:
            result += 1

    return n*m - result
print(solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]))
