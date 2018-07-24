# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        newhead, head, newhead.next = head, head.next, None
        tail = newhead
        while head:
            temp, head = head, head.next
            if temp.val<=newhead.val:
                temp.next, newhead = newhead, temp
            elif temp.val>=tail.val:
                tail.next, temp.next, tail = temp, None, temp
            else:
                cur =newhead
                while cur.next and cur.next.val<=temp.val:
                    cur = cur.next
                temp.next, cur.next = cur.next, temp                   
        return newhead