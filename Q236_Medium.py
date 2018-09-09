# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root in (None, p, q): return root
        left, right = (self.lowestCommonAncestor(kid, p, q)
                       for kid in (root.left, root.right))
        return root if left and right else left or right
#         AnceDict = {}
#         if not root: return None
#         if not p or not q: return None
#         if p==q: return p.val
#         AnceDict[root] = None
#         self.findAnce(root,AnceDict)
#         pList=[]
#         cur = p
#         while cur:
#             pList.append(cur.val)
#             cur = AnceDict[cur]
#         cur = q
#         # print(AnceDict[cur].val)
#         while cur:
#             if cur.val in pList:
#                 return cur
#             cur = AnceDict[cur]
            
        
        
#     def findAnce(self, root, AnceDict):
#         if not root:
#             return
#         if root.left:
#             AnceDict[root.left] = root
#             self.findAnce(root.left, AnceDict)
#         if root.right:
#             AnceDict[root.right] = root
#             self.findAnce(root.right, AnceDict)
    