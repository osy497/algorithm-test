#!/bin/python3

n = int(input())
arr1 = input().split()
arr2 = input().split()

result = []
for i in range(n):
    print(int(arr1[i]) | int(arr2[i]))
    result.append(int(arr1[i]) | int(arr2[i]))


for e in result:
    tmp = e
    tmp_list = []
    while tmp:
        if tmp % 2 == 1:
            tmp_list.append("#")
        else:
            tmp_list.append(" ")
        tmp = tmp//2
    print(tmp_list[::-1])

        


