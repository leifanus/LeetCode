class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Sieve of Eratosthenes
        if n<2: return 0
        count = 0
        l = [1]*n
        l[0] = l[1]= 0
        i = 2
        while i < n**0.5:
            l[2*i:n:i] = [0]*((n-1)/i-1)
            i += 1
            while l[i]==0:
                i+=1
        return l.count(1)