class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums) == 0:
            return False
        
        num_map = {}

        for i in range(len(nums)):
            if nums[i] in num_map:
                return True
            else:
                num_map[nums[i]] = 1

        return False