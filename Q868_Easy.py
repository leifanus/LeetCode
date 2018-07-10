class Solution(object):
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        out = []
        
        for j in range(len(A[0])):
            row = []
            for i in range(len(A)):
                row.append(A[i][j])
            out.append(row)
        return out