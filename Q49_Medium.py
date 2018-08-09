class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dic = {}
        for str in strs:
            s = ''.join(sorted(str))
            if s not in dic:
                dic[s]=[str]
            else:
                dic[s].append(str)
        return [dic[i] for i in dic]