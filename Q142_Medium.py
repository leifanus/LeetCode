# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # dic={}
        # cur = head
        # while cur:
        #     if id(cur) not in dic:
        #         dic[id(cur)] = cur
        #     else:
        #         return cur 
        #     cur = cur.next
        # return None
        # no Extra Space
        # Solution 2: Use math to derive the position.
        # Note that in this case, the two pointers must start from the head.
        slow = head
        fast = head
        first = True # Just for entering the first loop.
        while fast and fast.next and (first or slow != fast):
            first = False
            slow = slow.next
            fast = fast.next.next
        if not fast or not fast.next:
            return None
        # Otherwise, there must be a cycle. Let fast pointer points to head.
        fast = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow