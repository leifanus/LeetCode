class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if i==0 and j>0 and j<=n-1:
                    grid[i][j] += grid[i][j-1]
                elif j==0 and i>0 and i<=m-1:
                    grid[i][j] += grid[i-1][j]
                elif i>0 and i<=m-1 and j >0 and j<=n-1:
                    grid[i][j] += min(grid[i-1][j], grid[i][j-1])
        return grid[-1][-1]