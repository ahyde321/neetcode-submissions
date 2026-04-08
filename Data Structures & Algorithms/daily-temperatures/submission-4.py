class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        stack = [] # [temp, index]
        res = [0] * len(temperatures)

        for i, t in enumerate(temperatures):

            while stack and stack[-1][0] < t:
                stackT, stackI = stack.pop()
                res[stackI] = i - stackI
            
            stack.append([t, i])
        
        return res


    # [30, 38, 30, 36, 35, 40, 28]
    # [1, 4, 1, 2, 1, 0, 0]

    # [[40, 5], [28, 5]] 