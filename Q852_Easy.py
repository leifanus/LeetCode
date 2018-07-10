class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        # O(N)
#         for i in range(len(A)-1):
#             if A[i]>A[i+1]:
#                 return i
        
#         return None
#       O(logN)
        head, tail = 0, len(A)-1
        while head<tail-1:
            mid = (head+tail)//2
            if A[mid] < A[mid+1]:
                head = mid
            else:
                tail = mid
        return tail