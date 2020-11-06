class Solution:
    def longestPalindrome(self, s: str) -> str:
        s_list = list(s)
        for i in range(len(s_list)):
            for j in range(len(s_list), i):
                if s_list[i] == s_list[j]:
                    while i < j:
                        i += 1
                        j -= 1
            
