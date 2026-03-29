class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        for row in matrix:
            if target >= row[0] and target <= row[len(row)-1]:
                l, r = 0, len(row) - 1
                while l <= r:
                    mid = (l + r) // 2
                    if row[mid] > target:
                        r = mid - 1
                    elif row[mid] < target:
                        l = mid + 1
                    else:
                        return True
                
        return False