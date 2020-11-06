#!/bin/python3
import sys
size = 0
inp = ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]
l = dict()
count = 1
result = 0
for e in inp:
    if e in l.keys():
        result += 1
        l[e] = count
        count += 1
    else:
        #remove cache
        if size == 0:
            count += 1
            result += 5
            continue
            
        elif len(l) >= size:
            m = min(l.values())
            for ee in l.keys():
                if l[ee] == m:
                    del l[ee]
                    break
        #add cache
        l[e] = count
        count += 1
        result += 5

        
print(result)

            

            
    
