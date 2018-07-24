# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if not head:
            return head
        if not head.next:
            return TreeNode(head.val)
        preMid = self.preMid(head)
        ListMid = preMid.next
        TreeMid = TreeNode(ListMid.val)
        righthead = ListMid.next
        preMid.next = None
        TreeMid.left = self.sortedListToBST(head)
        TreeMid.right = self.sortedListToBST(righthead)
        return TreeMid
        
        
    def preMid(self, head):
        slow, fast = None, head
        if not head.next.next:
            return head
        while fast.next and fast.next.next:
            if not slow:
                slow, fast = head, fast.next.next
            else:
                slow, fast = slow.next, fast.next.next
        return slow