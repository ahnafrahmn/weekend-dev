class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if target < matrix[0][0] or matrix[-1][-1] < target: return False
        le = len(matrix)
        for i in range(le-1, -1, -1):
            if target >= matrix[i][0]:
                return True if target in matrix[i] else False