class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if len(matrix)==0:
            return []
        M, N = len(matrix), len(matrix[0])
        u, d, l, r = 0, M-1, 0, N-1
        lst = []
        # print(u,d,l,r)
        while d>=u and r>=l:
            for j in range(l, r+1):
                lst.append(matrix[u][j])
            u+=1
            if d>=u and r>=l:
                for i in range(u,d+1):
                    lst.append(matrix[i][r])
                r-=1
            if d>=u and r>=l:
                for j in range(r, l-1, -1):
                    lst.append(matrix[d][j])
                d-=1
            if d>=u and r>=l:
                for i in range(d, u-1, -1):
                    lst.append(matrix[i][l])
                l+=1
        return lst