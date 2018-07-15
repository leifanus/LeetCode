# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2
        if not l2:
            return l1
        #get smaller node as shead, the other as longer head
        if l1.val<l2.val:
            head = l1
            lCur = l2
        else:
            head = l2
            lCur = l1
        sCur = head.next
        Cur = head
        while sCur:
            if sCur.val < lCur.val:
                Cur = sCur
                sCur = sCur.next
            else:
                Cur.next = lCur
                Cur = Cur.next
                lCur = sCur
                sCur = Cur.next
        Cur.next = lCur
        return head