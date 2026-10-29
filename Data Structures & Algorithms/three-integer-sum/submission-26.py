class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        nums.sort()

        for i, a in enumerate(nums):

            if i > 0 and nums[i - 1] == a:
                continue
            
            l, r = i + 1, len(nums) - 1

            while l < r:
                
                b, c = nums[l], nums[r]
                total = a + b + c

                if total == 0:
                    res.append([a, b, c])
                    r -= 1
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                        
                elif total < 0:
                    l += 1
                else:
                    r -= 1
        return res