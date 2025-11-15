class Solution(object):
    def searchInsert(self, n, t):
        if len(n) == 1:
            return 0 if n[0]==t or t<n[0] else 1
        elif t < n[0] or t > n[-1]:
            return 0 if t<n[0] else len(n)
        l, r = 0, len(n)-1
        while l < r:
            if l == r-1:
                return l if n[l]==t else r
            m = (l+r)//2
            if n[m] == t:
                return m
            elif n[m] < t:
                l = m
            else:
                r = m
        