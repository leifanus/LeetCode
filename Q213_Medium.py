class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        N = len(nums)
        if N==0: return 0
        elif N==1: return nums[0]
        elif N==2: return max(nums[0], nums[1])
        else:
            return max(self.robHelper(nums[:-1]), self.robHelper(nums[1:]))

            
    def robHelper(self, nums):
        N = len(nums)
        dp=[0]*N
        if N==0: return 0
        elif N==1: return nums[0]
        elif N==2: return max(nums[0], nums[1])
        else:
            dp[0] = nums[0]
            dp[1] = max(nums[0], nums[1])
            for i in range(2, N):
                dp[i] = max(dp[i-1], dp[i-2]+nums[i])
            return dp[-1]