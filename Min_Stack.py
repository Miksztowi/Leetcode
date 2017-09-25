# -*- encoding:utf-8 -*-
# __author__=='Gan'


# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
# push(x) -- Push element x onto stack.
# pop() -- Removes the element on top of the stack.
# top() -- Get the top element.
# getMin() -- Retrieve the minimum element in the stack.
# Example:
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin();   --> Returns -3.
# minStack.pop();
# minStack.top();      --> Returns 0.
# minStack.getMin();   --> Returns -2.

class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min_stack = []
        self.min = float('inf')

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if not self.min_stack:
            self.min = float('inf')
        self.min_stack += x,
        self.min = min(self.min, x)

    def pop(self):
        """
        :rtype: void
        """
        _pop = self.min_stack.pop()
        if _pop == self.min:
            self.min = min(self.min_stack) if len(self.min_stack) > 0 else None
        return _pop

    def top(self):
        """
        :rtype: int
        """
        if len(self.min_stack) > 0:
            return self.min_stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.min

if __name__ == '__main__':
    # Your MinStack object will be instantiated and called as such:
    obj = MinStack()
    obj.push(1)
    obj.pop()
    param_3 = obj.top()
    param_4 = obj.getMin()


# 18 / 18 test cases passed.
# Status: Accepted
# Runtime: 79 ms
# Your runtime beats 74.41 % of python submissions.



# Use tuple
class MinStack:
    def __init__(self):
        self.q = []
    # @param x, an integer
    # @return an integer
    def push(self, x):
        curMin = self.getMin()
        if curMin == None or x < curMin:
            curMin = x
        self.q.append((x, curMin))

    # @return nothing
    def pop(self):
        self.q.pop()


    # @return an integer
    def top(self):
        if len(self.q) == 0:
            return None
        else:
            return self.q[len(self.q) - 1][0]


    # @return an integer
    def getMin(self):
        if len(self.q) == 0:
            return None
        else:
            return self.q[len(self.q) - 1][1]

