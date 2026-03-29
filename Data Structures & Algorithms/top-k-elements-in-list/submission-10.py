class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for i in range(len(nums)):
            count[nums[i]] = count.get(nums[i], 0) + 1
        
        for n, c in count.items():
            freq[c].append(n)
        
        for i in range(len(freq) - 1, 0, -1):
            
            for num in freq[i]:
                res.append(num)
                if k == len(res):
                    return res
