class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for item in tokens: 
            if item == '+': 
                a = stack.pop()
                b = stack.pop()
                stack.append(a + b)
            elif item == '-': 
                a = stack.pop()
                b = stack.pop()
                stack.append(b - a)
            elif item == '*': 
                a = stack.pop()
                b = stack.pop()
                stack.append(a * b)
            elif item == '/': 
                a = stack.pop()
                b = stack.pop()
                stack.append(int(b / a))
            else: 
                stack.append(int(item))
        return stack[-1]
        