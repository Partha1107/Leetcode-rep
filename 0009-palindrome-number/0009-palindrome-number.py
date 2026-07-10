class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False
            
        orginal = x

        revers_num = 0

        while x>0:
            temp = x%10
            revers_num = revers_num*10 + temp
            x //= 10
        
        return orginal == revers_num
