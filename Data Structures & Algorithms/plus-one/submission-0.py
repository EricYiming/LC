class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits) - 1, - 1, -1):
            d = digits[i]
            if d < 9: 
                digits[i] += 1
                return digits
            else: 
                digits[i] = 0
        res = [1]
        for d in digits: 
            res.append(d)
        return res



        