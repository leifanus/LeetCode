class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0:
            return False
        else:
            res = 0
            temp = x
            while x!=0:
                mod = x%10
                x= x/10
                res = res*10+mod
            return res==temp