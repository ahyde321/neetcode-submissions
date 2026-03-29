class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}

        for i in range(len(nums)):
            rem = target - nums[i]
            if rem in num_map:
                return [num_map.get(rem), i]
            num_map[nums[i]] = num_map.get(nums[i], i)

            
