class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        pre, cur =None, head
        while cur:
            if m<=1 and n >= 1:
                temp = cur.next
                if m==1:
                    start = cur
                    cur.next = None
                    last, cur = cur, temp
                else:
                    cur.next, cur, last = last, temp, cur
                m, n = m-1, n-1
                if n==0:
                    break
            else:
                pre, cur = cur, cur.next
                m, n = m-1, n-1
        if pre:               
            start.next, pre.next= cur, last   
        else:
            start.next = cur
            head = last
        return head