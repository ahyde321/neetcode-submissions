class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        res = []
        freq_map = {}
        buckets = [[] for i in range(len(nums)+1)]

        for num in nums:
            freq_map[num] = freq_map.get(num, 0) + 1
        
        for n, c in freq_map.items():
            buckets[c].append(n)
        
        for i in range(len(buckets) -1 , 0, -1):
            for val in buckets[i]:
                res.append(val)
            if len(res) == k:
                return res
        
        return -1

        
