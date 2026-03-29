class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []
        ops = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: a / b
        }

        for c in tokens:
            if c in ops:
                if len(stack) < 2:
                    return None
                num1 = int(stack.pop())
                num2 = int(stack.pop())
                stack.append(ops[c](num2, num1))
            else:
                stack.append(c)
        
        return int(stack[-1])