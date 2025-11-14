class Solution(object):
    def scoreOfString(self, s):
        i, j = 1, 0
        while i<len(s):
            j += abs(ord(s[i])-ord(s[i-1]))
            i += 1
        return j