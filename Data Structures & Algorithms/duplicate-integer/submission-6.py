class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        if len(nums) == 0:
            return False
        
        num_set = set()
        
        for i in range(len(nums)):
            if nums[i] in num_set:
                return True
            num_set.add(nums[i])
        
        return False