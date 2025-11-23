class Solution(object):
    def addDigits(self, n):
        return n%9 if n%9 else 9 if n>0 else 0