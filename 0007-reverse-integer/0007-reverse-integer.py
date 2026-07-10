class Solution(object):
    def reverse(self, x):
        sign = -1 if x < 0 else 1
        x = abs(x)

        reverse_integer = 0

        while x > 0:
            temp = x % 10
            reverse_integer = reverse_integer * 10 + temp
            x //= 10

        reverse_integer *= sign

        if reverse_integer < -2**31 or reverse_integer > 2**31 - 1:
            return 0

        return reverse_integer