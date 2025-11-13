class MinStack(object):

    def __init__(self):
        self.stack = []
        self.mi = float('inf')

    def push(self, val):
        if val < self.mi:
            self.mi = val
        self.stack.append(val)
        

    def pop(self):
        del self.stack[-1]
        

    def top(self):
        return self.stack[-1]
        

    def getMin(self):
        return self.mi if self.mi in self.stack else min(self.stack)