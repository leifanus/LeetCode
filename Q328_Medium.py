# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next or not head.next.next:
            return head
        else:
            odd, even = head, head.next
            cur = head.next.next
            while cur:
                temp = cur.next
                odd.next, even.next, cur.next = cur, temp, odd.next
                if not temp:
                    cur = temp
                else:
                    odd, even, cur= cur, temp, temp.next
            return head