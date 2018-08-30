class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums or len(nums)==1: return True
        target = len(nums)-1
        for i in range(len(nums)-1, -1, -1):
            if i + nums[i]>=target: target = i
        return target==0