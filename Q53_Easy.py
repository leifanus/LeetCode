class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        globalMax = nums[0]
        locMax = nums[0]
        for i in range(1,len(nums)):
            locMax = max(nums[i],locMax+nums[i])
            globalMax = max(globalMax,locMax)
        return globalMax