#!/bin/python3
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        s_list = list(s)
        length_list = []

        if len(s_list) == 0:
            return 0

        j = 1
        for i in range(len(s_list)):
            l = [s_list[i]]
            for j in range(i + 1, len(s_list)):
                if s_list[j] in l:
                    break
                l.append(s_list[j])


            length_list.append(len(l))
        return max(length_list)


