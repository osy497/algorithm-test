class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        l = r = 0
        answer = 0
        if not A:
            return 0
        diff = A[r] - A[r-1]
        for r in range(1, len(A)):
            length = r - l
            
            if diff != A[r] - A[r-1]:
                
                if r - 1 - l >= 2:
                    answer += ((r - 1 - l - 1) * (r - 1 - l))//2
                l = r - 1
            
            diff = A[r] - A[r-1]
            
        if r - l >= 2:
            answer += ((r - 1 - l) * (r - l))//2
        return answer
