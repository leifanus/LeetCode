class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        N = len(triangle)
        if N==0: return 0
        if N==1:
            M = len(triangle[0])
            if M==0: return 0
            if M==1: return triangle[0][0]
            else:
                return min(triangle[0])
        for i in range(1, N):
            M = len(triangle[i])
            for j in range(M):
                if j==0:
                    triangle[i][j] += triangle[i-1][j]
                elif j==M-1:
                    triangle[i][j] += triangle[i-1][j-1]
                else:
                    triangle[i][j] += min(triangle[i-1][j-1],triangle[i-1][j])
        return min(triangle[-1])