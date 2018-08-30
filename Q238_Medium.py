class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        l = [1]*n
        order = reverse = 1
        for i in range(n):
            l[i] *= order
            l[n-1-i] *= reverse
            order *= nums[i]
            reverse*=nums[n-1-i]
        return l