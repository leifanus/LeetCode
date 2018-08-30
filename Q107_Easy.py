# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: return []
        queue = []
        level = 0
        ans = [[]]
        queue.append((root, 0))
        while queue!=[]:
            node, level = queue.pop(0)
            if level<len(ans):
                ans[level].append(node.val)
            else:
                ans.append([node.val])
            if node.left:
                queue.append((node.left, level+1))
            if node.right:
                queue.append((node.right, level+1))
        ans.reverse()
        return ans