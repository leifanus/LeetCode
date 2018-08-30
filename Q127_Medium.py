class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        level = 1
        queue = [(beginWord, level)]
        seen = set([beginWord])
        wordList = set(wordList)
        while queue:
            word, level = queue.pop(0)
            for item in self.findNeighbour(word, wordList):
                if item == endWord:
                    return level+1
                elif item in seen:
                    continue
                seen.add(item)
                queue.append([item, level+1])
        return 0
                
            
    
        
        
    def findNeighbour(self, word, wordList):
        l = []
        for i in range(len(word)):
            for letter in string.ascii_lowercase:
                candidate = word[:i] + letter + word[i+1:]
                if candidate in wordList:
                    l.append(candidate)
        return l
#         ans = [0]
#         self.Helper(wordList, beginWord, endWord, [beginWord], ans)
#         return ans[0]
        
#     def Helper(self, wordList, beginWord, endWord, l, ans):
#         if beginWord == endWord:
#             if ans[0]==0 or len(l)<ans[0]:
#                 ans[0] = len(l)
#             # if len(l)<ans[0]:
#             #     ans[0] = len(l)
#             return 
#         for item in wordList:
#             if self.isLadder(item, beginWord) and item not in l:
#                 l.append(item)
#                 self.Helper(wordList, item, endWord, l, ans)
#                 l.pop()
#         # ans[0] = 0
#         return 
            
#     def isLadder(self, word1, word2):
#         flag = False
#         for i in range(len(word1)):
#             if word1[:i]+ word1[i+1:]==word2[:i]+word2[i+1:]:
#                 flag = True
#         return flag