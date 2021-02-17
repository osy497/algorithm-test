class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        answer = 0
        while l < r:
            size = (r - l) * min(height[r], height[l])
            answer = max(answer, size)
            if height[r] < height[l]:
                r -= 1
            else:
                l += 1
        return answer
            
        
