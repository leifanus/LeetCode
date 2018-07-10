# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
#         if head and head.next and head.next.next:        
#             prev = head
#             while prev.next and prev.next.next:
#                 ptail = self.beforetail(prev)
#                 tail = ptail.next
#                 tail.next = prev.next
#                 prev.next = tail
#                 ptail.next = None
#                 prev = tail.next
                   
        
#     def beforetail(self, head):
#         cur = head
#         while cur and cur.next and cur.next.next:
#             cur = cur.next
#         return cur
        if head and head.next and head.next.next:  
            val_list = []
            cur = head
            while cur:
                val_list.append(cur.val)
                cur = cur.next
            cur = head
            while cur and cur.next:
                cur.val = val_list.pop(0)
                cur = cur.next
                cur.val = val_list.pop()
                cur = cur.next
            if len(val_list)==1:
                cur.val = val_list.pop()
            