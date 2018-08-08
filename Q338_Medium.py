# from math import log
class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        if num == 0: return [0]
        dp = [0]*(num+1)
        dp[0] = 0
        dp[1] = 1
        for i in range(2, num+1):
            # dp[i] = 1+ dp[i-2**int(log(i)/log(2))]
            dp[i] = (1&i)+ dp[i>>1]
        return dp