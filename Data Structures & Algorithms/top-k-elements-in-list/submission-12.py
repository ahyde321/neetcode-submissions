class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = [[] for i in range(len(nums) + 1)]
        count = {} # num : count
        res = []

        for num in nums:
                count[num] = count.get(num, 0) + 1
        
        for c, v in count.items():
            freq[v].append(c)
        
        for i in range(len(freq) - 1, 0, -1):

            for val in freq[i]:
                res.append(val)
                if len(res) == k:
                    return res
        
        return -1


            
