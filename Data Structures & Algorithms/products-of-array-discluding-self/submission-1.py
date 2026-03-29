class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1
        suffix = 1
        arr = [1] * len(nums)

        # prefix
        for i in range(len(nums)):
            arr[i] *= prefix
            prefix *= nums[i]
        
        # suffix
        for i in range(len(nums) - 1, -1, -1):
            arr[i] *= suffix
            suffix *= nums[i]
        
        return arr