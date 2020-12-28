#!/bin/python3

def solution(food_times, k):
    answer = 0
    s = sum(food_times)
    length = len(food_times)
    cur_time = 0
    food_list = [i for i in range(length)]
    cur_idx = 0

    while s:
        print(food_times, food_list,length,"#",  cur_time, cur_idx)
        real_idx = cur_idx % length
        m = min(food_times)
        if cur_time == k:
            print("first ...")
            return food_list[real_idx] + 1
        elif cur_time < k and cur_time > k - m * length:
            print("second..")
            while cur_time < k:
                print(food_times, cur_time, length)
                real_idx = cur_idx % length
                food_times[real_idx] -= 1
                cur_time += 1
                s -= 1
                if s == 0:
                    return -1
                if food_times[real_idx] == 0:
                    del food_times[real_idx]
                    del food_list[real_idx]
                    length -= 1
                    continue
                cur_idx += 1
            return food_list[real_idx] + 1
        print("pass..")
        for i in range(length):
            food_times[i] -= m
        cur_time += m * length
        for i in range(length)[::-1]:
            if food_times[i] == 0:
                del food_times[i]
                del food_list[i]
                length -= 1
        print(food_times, length, cur_time)
        print("####")

    return -1


#for i in range(7):
#    print(i, solution([3, 1, 2], i))
print(1, solution([3, 1, 2], 4))
