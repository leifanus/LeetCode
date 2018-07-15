class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic={}
        for i in nums:
            if i in dic:
                dic[i] +=1
            else:
                dic[i] = 1
        maj = nums[0]
        for j in dic:
            if dic[maj]< dic[j]:
                maj = j
        return maj