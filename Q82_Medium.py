# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # idea is to manipulate the list, then assign the nodes with the value
        # in the list and discard the remaining nodes.
        # if not head:
        #     return None
        # else:
        #     cur = head        
        #     dic = {}
        #     l = []
        #     while cur:
        #         l.append(cur.val)
        #         if cur.val not in dic:
        #             dic[cur.val] = 1
        #         else:
        #             dic[cur.val] += 1
        #         cur = cur.next
        #     val_list = []
        #     for i in l:
        #         if dic[i]==1:
        #             val_list.append(i)
        #     if len(val_list)==0:
        #         return None
        #     else:
        #         cur = head
        #         for i in range(len(val_list)-1):
        #             cur.val = val_list[i]
        #             cur = cur.next
        #         cur.val = val_list[-1]
        #         cur.next = None
        #         return head
        dummy = ListNode(-1)
        dummy.next = head
        prev, curr = dummy, dummy.next
        
        while curr:
            if curr.next and curr.val == curr.next.val:
                val_to_rem = curr.val
                
                while curr and curr.val == val_to_rem:
                    curr = curr.next
                    
                prev.next = curr
                
            else:
                prev, curr = curr, curr.next
                
        return dummy.next