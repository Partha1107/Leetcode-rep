class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        n = len(s)

        # 1. Skip leading spaces
        while i < n and s[i] == ' ':
            i += 1

        # 2. Check sign
        sign = 1

        if i < n and s[i] == '-':
            sign = -1
            i += 1
        elif i < n and s[i] == '+':
            i += 1

        # 3. Read digits
        num = 0

        while i < n and s[i].isdigit():
            digit = int(s[i])

            num = num * 10 + digit

            # 4. Check overflow
            if sign == 1 and num > 2**31 - 1:
                return 2**31 - 1

            if sign == -1 and -num < -2**31:
                return -2**31

            i += 1

        return sign * num