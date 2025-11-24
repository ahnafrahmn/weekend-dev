class Solution(object):
    def isIsomorphic(self, s, t):
        d = {}
        for i, j in zip(s, t):
            if i in d and d[i]!=j:
                return False
            d[i] = j
        return True if len(set(s))==len(set(t)) else False