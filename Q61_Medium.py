# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        l = self.getLength(head)
        if head is not None and head.next is not None:
            for i in range(k%l):
                ptail = self.prevTail(head)
                ptail.next.next = head
                head = ptail.next
                ptail.next = None
        return head
            
    
    def getLength(self, head):
        if head == None:
            return 0
        else:
            return 1+self.getLength(head.next)
        
    def prevTail(self, head):
        curNode = head
        while curNode is not None and curNode.next is not None and curNode.next.next is not None:
            curNode = curNode.next
        return curNode