# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        
        # #deep copy of original list regardless of random part
        # cur = head
        # newhead = None
        # node_list = []
        # newnode_list = []
        # while cur is not None:
        #     node_list.append(cur)
        #     newNode = RandomListNode(cur.label)
        #     newnode_list.append(newNode)
        #     if newhead is None:
        #         newhead = newNode
        #         newCur = newNode
        #     else:
        #         newCur.next = newNode
        #         newCur = newCur.next
        #     cur = cur.next
        # #get tracking idx of the random part
        # cur = head
        # track_idx = []
        # while cur is not None:
        #     if cur.random is None:
        #         track_idx.append(-1)
        #     else:
        #         track_idx.append(node_list.index(cur.random))
        #     cur = cur.next
        # #update our new list
        # newCur = newhead
        # for k in track_idx:
        #     if k is -1:
        #         newCur.random = None
        #     else:
        #         newCur.random = newnode_list[k]
        #     newCur = newCur.next
        # return newhead
        
        if not head:
            return None
        dic = {}
        cur = head
        while cur:
            newNode = RandomListNode(cur.label)
            dic[cur] = newNode
            cur = cur.next
        cur = head
        while cur:
            if cur.next:
                dic[cur].next = dic[cur.next]
            else:
                dic[cur].next = None
            if cur.random:
                dic[cur].random = dic[cur.random]
            else:
                dic[cur].random = None            
            cur = cur.next
        return dic[head]