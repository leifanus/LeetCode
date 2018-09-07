class Solution:
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or len(matrix)==0:
            return 0
        M, N = len(matrix), len(matrix[0])
        dp = [0]*(N+1)
        ans = prev = 0
        for i in range(1,M+1):
            for j in range(1,N+1):
                temp = dp[j]
                if matrix[i-1][j-1]=="1":
                    dp[j] = min(min(dp[j-1], prev),dp[j])+1
                    ans = max(ans, dp[j])
                else:
                    dp[j]=0
                prev = temp
        return ans**2