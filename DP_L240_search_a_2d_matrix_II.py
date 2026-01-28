class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])

        # start at top right corner or bottom left corner, forms a binary search array
        i, j = 0, n-1

        while i<m and j>=0:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                # reduce column by moving left
                j-=1
            else:
                # reduce row by moving down
                i+=1
        return False