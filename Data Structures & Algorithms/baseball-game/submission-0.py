class Solution:
    def calPoints(self, operations: List[str]) -> int:
        total = []
        for op in operations: 
            if op == "+": 
                a = total[-1]
                b = total[-2]
                total.append(a + b)
            elif op == "C": 
                total.pop()
            elif op == "D": 
                total.append(total[-1] * 2)
            else: 
                total.append(int(op))
        return sum(total)

        