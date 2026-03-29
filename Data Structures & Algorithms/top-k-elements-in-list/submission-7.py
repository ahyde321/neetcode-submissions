class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq_map = {}
        freq_arr = [[] for i in range(len(nums)+1)]
        res = []

        for num in nums:
            freq_map[num] = freq_map.get(num, 0) + 1
        for f, v in freq_map.items():
            freq_arr[v].append(f)
        
        for i in range(len(freq_arr)-1, 0, -1):
            for num in freq_arr[i]:
                res.append(num)
            if len(res) == k:
                return res





        # create an array for items of a freq n
        # create an array of arrays to hold all array of items of freq n
        # loop backwards through array of arrays to find k most freq nums

