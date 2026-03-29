class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums) <= 1:
            return False
        
        hashset = set()

        for i in range(len(nums)):
            print(i)
            if nums[i] in hashset:
                return True
            hashset.add(nums[i])
        
        return False
