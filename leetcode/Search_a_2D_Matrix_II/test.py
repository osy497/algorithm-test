class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        l = 0
        r = m - 1
        while l <= r:
            m = (l + r)//2
            if matrix[m][0] == target:
                return True
            elif matrix[m][0] < target:
                l = m + 1
            else:
                r = m - 1
        end = r
        for i in range(end + 1):
            l = 0
            r = n - 1
            while l <= r:
                m = (l + r)//2
                if matrix[i][m] == target:
                    return True
                elif matrix[i][m] < target:
                    l = m + 1
                else:
                    r = m - 1
        return False
        
        
