class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        # through through array, compare target with largest value in each
        # if less, search that array: set l as min and r as max, run binary search
        # if its found retutn true else Falsr
        row = None
        for i in range(len(matrix)):
            if target <= matrix[i][-1]:
                row = i
                break
        
        if row is None:
            return False
        
        l, r = 0, len(matrix[row]) - 1
        while l <= r:
            mid = (l + r) // 2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        
        return False
        

        



        