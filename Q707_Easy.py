class MyLinkedList(object):
    
    class ListNode(object):
        def __init__(self, val):
            self.val = val
            self.next = None
            
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        cur = self.head
        while cur and index>0:
            cur = cur.next
            index -=1
        if index ==0 and cur is not None:
            return cur.val
        else:
            return -1
            
            

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: void
        """
        node = self.ListNode(val)
        node.next = self.head
        self.head = node
        

    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: void
        """
        cur = self.head
        node = self.ListNode(val)
        if not cur:
            self.head = node
        else:
            while cur.next:
                cur=cur.next
            cur.next = node
        
        

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: void
        """
        cur = self.head
        node = self.ListNode(val)
        if index==0:
            self.addAtHead(val)
        elif index>0:
            while cur and index>1:
                cur = cur.next
                index -= 1
            if index==1 and cur is not None:
                if cur.next is not None:
                    node.next, cur.next = cur.next, node
                else:
                    cur.next = node
        
        

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: void
        """
        cur = self.head
        if index==0:
            self.head = self.head.next
        elif index>0:
            while cur and index>1:
                cur = cur.next
                index -= 1
            if index==1 and cur is not None:
                if cur.next is not None:
                    temp = cur.next
                    cur.next, temp.next = temp.next, None 
                    
        
    # def ListNode(self, val):
    #     self.val = val
    #     self.next = None
        

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)