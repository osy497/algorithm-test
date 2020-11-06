#!/bin/python3


inp = list(input())

result = 0
flag = 0
l = []
score = []
index = 0
for e in inp:
    if e == "S":
        score.append(int(''.join(l)))
        index += 1
        l = []
    elif e == "D":
        score.append(int(''.join(l)) ** 2)
        index += 1
        l = []
    elif e == "T":
        score.append(int(''.join(l)) ** 3)
        index += 1
        l = []
    elif e == "*":
        score[index-1] *= 2
        if index > 1:
            score[index-2] *= 2
    elif e == "#":
        score[index-1] *= -1
    else:
        l.append(e)
    print(score)


for e in score:
    result += e



print(result)
