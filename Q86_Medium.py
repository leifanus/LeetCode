# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        #maintain two list
        if not head or not head.next:
            return head
        cur = head
        scur = shead = None
        lcur = lhead = None
        while cur:
            if cur == head:
                if cur.val<x:
                    scur= shead = cur
                else:
                    lcur = lhead = cur
            else:
                if cur.val < x:
                    if not shead:
                        scur= shead = cur
                    else:
                        scur.next = cur
                        scur = scur.next
                else:
                    if not lhead:
                        lcur = lhead = cur
                    else:
                        lcur.next = cur
                        lcur = lcur.next                 
            cur = cur.next
        if shead:
            scur.next = lhead
        else:
            shead = lhead
        if lhead:
            lcur.next = None
        return shead