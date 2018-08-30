class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        N = len(prices)
        dp = [0]*N
        if N==0 or N==1:
            return 0
        dp[0] = 0
        mini = prices[0]
        for i in range(1, N):
            dp[i] = max(dp[i-1], prices[i]-mini)
            if prices[i]<mini:
                mini = prices[i]
        return dp[N-1]