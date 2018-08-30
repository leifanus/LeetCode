class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        INT_MIN = -2**31
        INT_MAX = 2**31-1
        
        split = str.split()
        if len(split)==0: return 0
        
        s = split[0]
        flag = True
        
        if not s[0].isnumeric() and s[0]!='-' and s[0]!='+':
            return 0
        if s[0]=='-':
            s = s[1:]
            flag = False
        elif s[0]=='+':
            s = s[1:]
        if s=='': return 0
        res = ""
        r = 0
        num = s[0]
        N = len(s)
        while num.isnumeric() and r<N:
            res += num
            r += 1
            if r<N:
                num = s[r]          
        if res=="": return 0
        else:
            res = (2*flag-1)*int(res)

        if res > INT_MAX:
            res = INT_MAX
        if res < INT_MIN:
            res = INT_MIN
        return res