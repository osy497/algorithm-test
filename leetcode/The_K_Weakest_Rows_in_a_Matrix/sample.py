class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        answer = sorted([[sum(x), i] for i, x in enumerate(mat)])
        return [x[1] for x in answer[:k]]
        
