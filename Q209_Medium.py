class Solution:
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        total = left = 0
        ans = len(nums)+1
        for right, n in enumerate(nums):
            total += n
            while total>=s:
                ans = min(ans, right-left+1)
                total -= nums[left]
                left+=1
        return 0 if ans>len(nums) else ans