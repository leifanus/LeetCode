class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        ans = []
        N = len(path)
        l = path.split('/')
        for i in range(len(l)):
            if l[i]!="." and l[i]!=".." and l[i]!="":
                ans.append(l[i])
            elif l[i]=='..' and len(ans)!=0:
                ans.pop()
        return '/'+'/'.join(ans)