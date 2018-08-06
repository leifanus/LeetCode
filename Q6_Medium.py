class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        left = 2*numRows - 4
        right = 2
        N = len(s)
        if N<=numRows or numRows==1:
            return s
        
        out = ""
        i=j=1
        while left>0:
            count = 0
            while i<N:
                out += s[i]
                if count%2==0:
                    i+=left
                else:
                    i+=right
                count += 1
            left -= 2
            right += 2
            j+=1
            i = j
        return s[::2*numRows-2]+out+s[numRows-1::2*numRows-2]