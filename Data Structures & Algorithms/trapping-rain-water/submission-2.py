class Solution:
    def trap(self, height: List[int]) -> int:

        if not height: return 0

        l, r = 0, len(height) - 1
        maxL, maxR = height[l], height[r]
        area = 0

        while l < r:
            if maxL < maxR:
                l +=1
                maxL = max(maxL, height[l])
                area += maxL - height[l]
            else:
                r -= 1
                maxR = max(maxR, height[r])
                area += maxR - height[r]
        
        return area
            

# [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
# min(l, r) - h[i]



        