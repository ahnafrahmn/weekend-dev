class Solution(object):
    def recoverOrder(self, o, f):
        return [i for i in o if i in f]