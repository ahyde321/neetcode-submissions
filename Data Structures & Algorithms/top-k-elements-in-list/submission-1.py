class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        num_map = {}
        for num in nums:
            num_map[num] = num_map.get(num, 0) + 1
        
        k_nums = sorted(num_map, key=num_map.get, reverse=True)[:k]
        return k_nums
        