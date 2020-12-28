#!/bin/python

CHECK=list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
str1 = "aa1+aa2"
str2 = "AAAA12"

sub_str1 = []
str1_list = list(str1)
for i in range(len(str1_list) - 1):
    tmp = str1_list[i] + str1_list[i+1]
    if not str1_list[i].upper() in CHECK:
        continue
    if not str1_list[i+1].upper() in CHECK:
        continue

    sub_str1.append(tmp.upper())

sub_str2 = []
str2_list = list(str2)
for i in range(len(str2_list) - 1):
    tmp = str2_list[i] + str2_list[i+1]
    if not str2_list[i].upper() in CHECK:
        continue
    if not str2_list[i+1].upper() in CHECK:
        continue

    sub_str2.append(tmp.upper())

       
map_str1 = dict()
for e in sub_str1:
    if e in map_str1.keys():
        map_str1[e] += 1
    else:
        map_str1[e] = 1
map_str2 = dict()
for e in sub_str2:
    if e in map_str2.keys():
        map_str2[e] += 1
    else:
        map_str2[e] = 1



intersect = 0
union = 0

tmp_set = set()
for e1 in map_str1.keys():
    for e2 in map_str2.keys():
        if e1 == e2:
            intersect += min(map_str1[e1], map_str2[e2])
        tmp_set.add(e1)
        tmp_set.add(e2)

for e in tmp_set:
    if e in map_str1.keys() and e in map_str2.keys():
        union += max(map_str1[e], map_str2[e])
    elif e in map_str1.keys():
        union += map_str1[e]
    else:
        union += map_str2[e]

if union == 0:
    print(66536)
else:
    print(intersect * 66536 // union)
