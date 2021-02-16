class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        answer = []
        nums = "0123456789"
        def helper(idx, cur):
            if idx >= len(S):
                answer.append(cur)
                return
            if S[idx] in nums:
                helper(idx + 1, cur + S[idx])
            else:
                helper(idx + 1, cur + S[idx].upper())
                helper(idx + 1, cur + S[idx].lower())
        helper(0, "")
        return answer
        
