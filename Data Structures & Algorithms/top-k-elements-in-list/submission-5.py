class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        arr = [[] for i in range(len(nums)+1)]
        count = {}
        output = []

        for i in range(len(nums)):
            count[nums[i]] = count.get(nums[i], 0) + 1
        
        for n, c in count.items():
            arr[c].append(n)
        
        for i in range(len(arr)-1, 0, -1):
            for j in arr[i]:
                output.append(j)
            if len(output) == k:
                return output


        
        
        