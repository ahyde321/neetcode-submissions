class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        num_map = {}

        for i, n in enumerate(nums):
            rem = target - n
            if rem in num_map:
                return [num_map[rem], i]
            num_map[n] = i
            
        

            
            
        