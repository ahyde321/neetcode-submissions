class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []
        ops = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: float(a) / b
        }

        for c in tokens:
            if c in ops:
                a, b = stack.pop(), stack.pop()
                stack.append(int(ops[c](b, a)))
            else:
                stack.append(int(c))
        
        return stack[-1]