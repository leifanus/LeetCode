class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        time = 0
        l = len(timeSeries)
        if l==0:
            return 0
        for i in range(l-1):
            time+=min(timeSeries[i+1]-timeSeries[i], duration)
        time+=duration
        return time