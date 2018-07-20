class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        max_row = [max(item) for item in grid]
        # max_col = [max(row[i] for row in grid) for i in range(len(grid[0]))]
        max_col=[]
        for i in range(len(grid[0])):
            col = [item[i] for item in grid]
            max_col.append(max(col))
        result = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                result = result + min(max_row[i], max_col[j]) - grid[i][j]
        return result
#         row_maxes = [max(row) for row in grid]
#         col_maxes = [max(col) for col in zip(*grid)]

#         return sum(min(row_maxes[r], col_maxes[c]) - val
#                    for r, row in enumerate(grid)
#                    for c, val in enumerate(row))