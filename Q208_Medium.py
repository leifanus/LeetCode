class TrieNode:
    def __init__(self):
        self.children = [None]*26
        self.isEndOfWord = False     
        
class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = self.getNode()
        
    def getNode(self):
        return TrieNode()
        
    def _charToIndex(self, ch):
        return ord(ch)- ord('a')
    
    
    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        cur = self.root
        N = len(word)
        for level in range(N):
            idx = self._charToIndex(word[level])
            if not cur.children[idx]:
                cur.children[idx] = self.getNode()
            cur = cur.children[idx]
        cur.isEndOfWord = True
        

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        cur = self.root
        N = len(word)
        for level in range(N):
            idx = self._charToIndex(word[level])
            if not cur.children[idx]:
                return False
            cur = cur.children[idx]
        return cur.isEndOfWord
        

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        cur = self.root
        N = len(prefix)
        for level in range(N):
            idx = self._charToIndex(prefix[level])
            if not cur.children[idx]:
                return False
            cur = cur.children[idx]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)