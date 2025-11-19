class Solution(object):
    def strStr(self, h, n):
        return h.index(n) if n in h else -1