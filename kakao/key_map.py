#!/bin/python3
import copy
def solution(key, lock):
    answer = False
    #make 7 x 7
    lock_size = len(lock)
    key_size = len(key)
    a = len(lock) + (len(key) - 1) * 2
    m_lock = [[0] * a for _ in range(a)]
    for i in range(len(key) - 1, len(lock) + len(key) - 1):
        for j in range(len(key)-1, len(lock) + len(key)-1):
            m_lock[i][j] += lock[i-len(key)+1][j-len(key)+1]

    for _ in range(4):

        for i in range(lock_size + key_size - 1):
            for j in range(lock_size + key_size - 1):
                tmp = copy.deepcopy(m_lock)
                for ii in range(key_size):
                    for jj in range(key_size):
                        tmp[i+ii][j+jj] += key[ii][jj]
                answer = True
                for ii in range(key_size - 1, lock_size + key_size - 1):
                    for jj in range(key_size - 1, lock_size + key_size - 1):
                        if tmp[ii][jj] != 1:
                            answer = False
                if answer:
                    return answer
        tmp_key = [[0] * key_size for _ in range(key_size)]
        for i in range(key_size):
            for j in range(key_size):
                tmp_key[i][j] = key[j][key_size-1-i]
        key = tmp_key
    return answer

#print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))
print(solution([[0, 0, 0, 0], [1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]], [[1, 1, 1, 1], [0, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]))
