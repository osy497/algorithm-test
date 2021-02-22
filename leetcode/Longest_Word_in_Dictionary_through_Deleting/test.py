class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        def helper(a, b):
            
            j = 0
            answer = ""
            for i in range(len(a)):
               # print(a[i], b[j])
                if a[i] == b[j]:
                    answer += a[i]
                    j += 1
                if j >= len(b):
                    break
            #print(answer)
            if len(b) == j:
                return answer
            return ""
        answer = ""
        
        for word in d:
            answer = min(answer, helper(s, word), key=lambda x: (-len(x), x))
            #answer = max(answer, helper(s, word), key=lambda x: (len(x), x))
        return answer
                    
        
