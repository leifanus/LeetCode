# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        l1=[]
        l2=[]
        self.getList(root1,l1)
        self.getList(root2,l2)
        print(l1, l2)
        return l1==l2
        
    def getList(self, root, l):
        if not root.left and not root.right:
            l.append(root.val)
        elif not root.left:
            self.getList(root.right, l)
        elif not root.right:
            self.getList(root.left, l)
        else:
            self.getList(root.left, l)
            self.getList(root.right, l)