class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxnum, num, ss = 0, 0, ''
        for i in s:
            if i in ss:
                ss = ss.split(i)[-1]+i
                num = len(ss)
            else:
                num+=1
                ss+=i
                if num>maxnum:
                    maxnum=num
        return maxnum