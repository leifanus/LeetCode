class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0]*(n+1)
        if n==0:
            return 1
        if n==1:
            return 10
        dp[0] = 1
        dp[1] = 10
        for i in range(2,n+1):
            dp[i] = dp[i-1] + self.fact(i)
        return dp[n]
    
    def fact(self, i):
        if i>10:
            return 0
        elif i==2:
            return 81
        else:
            out = 81
            num = 8
            while i>2:
                out*=num
                num-=1
                i-=1
            return out