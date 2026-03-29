class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq = [[] for num in range(len(nums) + 1)]
        count = {}

        for i in range(len(nums)):
            count[nums[i]] = count.get(nums[i], 0) + 1
        
        for n, v in count.items():
            freq[v].append(n)
        
        output = []

        for i in range(len(freq) - 1, -1, -1):
            for num in freq[i]:
                output.append(num)
            if len(output) == k:
                return output
        