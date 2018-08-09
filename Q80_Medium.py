class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        N= len(nums)
        if N==0:
            return 0
        num = nums[0]
        count = i = 1
        happen = 0
        while i + happen < N:
            if nums[i]==num:
                count+=1
            else:
                num = nums[i]
                count = 1
            if count==3:
                happen += 1
                count -= 1
                if i < N-1:
                    nums[i:-1], nums[-1] = nums[i+1:], nums[i]
            else:
                i+=1
        return N-happen