#!/bin/python3


n = 10
t = 60
m = 45
#timetable = ["23:59", "23:59","23:59","23:59","23:59","23:59","23:59","23:59","23:59","23:59","23:59","23:59","23:59","23:59","23:59","23:59"]
timetable = ["23:59", "23:59", "23:59", "23:59", "23:59"]

def cal(time, lat, opt):
    h, m = map(int, time.split(":"))
    if opt == 1: #plus
        m += lat
        if m >= 60:
            m -= 60
            h += 1
        if h >= 24:
            h -= 24
    elif opt == -1: #minus
        m -= lat
        if m < 0:
            m += 60
            h -= 1
        if h < 0:
            h += 24

    if h < 10:
        rh = "0" + str(h)
    else:
        rh = str(h)
    if m < 10:
        rm = "0" + str(m)
    else:
        rm = str(m)

    return rh + ":" + rm

def comp(a, b):
    ah, am = map(int, a.split(":"))
    bh, bm = map(int, b.split(":"))
    if ah < bh:
        return 1
    elif ah == bh and am < bm:
        return 1
    elif ah == bh and am > bm:
        return -1
    elif ah > bh:
        return -1
    else:
        return 0

def min_time(timetable):
    mtime = "25:60"
    for time in timetable:

        if comp(time, mtime) == 1:
            mtime = time
    return mtime



lat = 0
table = []
start = "09:00"
start = cal(start, t, -1)
for i in range(n):
    
    tmp = cal(start, t, 1)
    table = table + [tmp] * m
    start = tmp

last_bus = table[-1]
    
ii = 0
while timetable:
    m = min_time(timetable)

    for i in range(len(table)):
        if comp(m, table[i]) != -1:
            del table[i]
            break


    for i in range(len(timetable)):
        if timetable[i] == m:
            prior = timetable[i]
            del timetable[i]
            break



if last_bus in table:
    result = last_bus
else:
    result = cal(prior, 1, -1)

print(result)
    
