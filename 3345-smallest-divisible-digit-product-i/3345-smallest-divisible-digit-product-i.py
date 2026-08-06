class Solution(object):
    def smallestNumber(self, n, t):

        current = n

        while True:

            product = 1
            temp = current

            while temp > 0:
                digit = temp % 10
                product *= digit
                temp //= 10

            if product % t == 0:
                return current

            current += 1