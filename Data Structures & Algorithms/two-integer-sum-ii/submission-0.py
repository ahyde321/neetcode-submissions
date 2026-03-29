class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        for i in range(len(numbers)):
            rem = target - numbers[i]
            if rem in numbers:
                if numbers.index(rem) != i:
                    ans = [i, numbers.index(rem)]
                    ans = sorted([x+1 for x in ans])
                    return ans
        