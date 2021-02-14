class Solution:
    def findLHS(self, nums: List[int]) -> int:
        answer = 0
        d = {}
        for num in nums:
            if num in d:
                d[num] += 1
            else:
                d[num] = 1
        for k in d.keys():
            if k - 1 in d:
                answer = max(answer, d[k] + d[k-1])
            if k + 1 in d:
                answer = max(answer, d[k] + d[k+1])
        return answer
