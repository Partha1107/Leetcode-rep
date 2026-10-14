class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
       
        if sum > 9 * num or sum < 1:
            return ""

        digits = []

        for i in range(num):
            if sum > 0:
                digit = min(9, sum)
                digits.append(digit)
                sum -= digit
            else:
                digits.append(0)  

        if digits[0] == 0:
            for i in range(1, num):
                if digits[i] > 0:
                    digits[i] -= 1
                    digits[0] = 1
                    break

        return ''.join(map(str, digits))
