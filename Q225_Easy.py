class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.l=[]
        self.l2=[]

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        self.l.append(x)

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        while len(self.l)>1:
            self.l2.append(self.l.pop(0))
        x = self.l.pop(0)
        self.l = self.l2
        self.l2=[]
        return x
        
        

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        return self.l[-1]

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return self.l==[]


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()