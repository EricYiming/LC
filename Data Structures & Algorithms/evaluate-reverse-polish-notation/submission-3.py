class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        values = []
        for item in tokens: 
            if item == '+': 
                val1 = values.pop()
                val2 = values.pop()
                values.append(val1 + val2)
            
            elif item == '-': 
                val1 = values.pop()
                val2 = values.pop()
                values.append(val2 - val1)
            
            elif item == '*': 
                val1 = values.pop()
                val2 = values.pop()
                values.append(val1 * val2)
            
            elif item == '/': 
                val1 = values.pop()
                val2 = values.pop()
                values.append(int(val2/val1) )
            
            else: 
                values.append(int(item))
        return values[-1]
