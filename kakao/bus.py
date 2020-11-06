#!/bin/python3


n = 10
t = 60
m = 45
timetable = ["23:59", "23:59","23:59","23:59","23:59","23:59","23:59","23:59","23:59","23:59","23:59","23:59","23:59","23:59","23:59","23:59"]
#timetable = ["00:01", "00:01", "00:01", "00:01", "00:01"]

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

ii = 0
result = "-1:-1"
while timetable:
    #find time for the last one seat
    a = min_time(timetable)

    if (n * m - ii) == 2: # one seat
        result = cal(a, 1, -1)
        break

    for i in range(len(timetable)):
        if a == timetable[i]:
            del timetable[i]
            break
    ii += 1

        # result = time(n * m) - 1

time = "09:00"
for _ in range(n - 1):
    time = cal(time, t, 1)

if result == "-1:-1":
    result = time#last time of bus
    


print(result)
