class Solution(object):
    def inc(self, s):
        pre = s[0]
        for i in s[1:]:
            if i < pre:
                return False
            pre = i
        return True


    def dec(self, s):
        pre = s[0]
        for i in s[1:]:
            if i > pre:
                return False
            pre = i
        return True


    def isMonotonic(self, s):
        if len(s) < 3:
            return True
        elif min(s)==s[0] and max(s)==s[-1]:
            return self.inc(s)
        elif max(s)==s[0] and min(s)==s[-1]:
            return self.dec(s)
        else:
            return False