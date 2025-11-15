class Solution(object):
    def mySqrt(self, x):
        t = [0, 1, 2, 3]
        if x in t:
            return 0 if x==0 else 1
        l , r = 1, x//2
        while l < r:
            if l == r-1:
                return l if (l*l < x or l*l == x) and r*r > x else r
            m = (l+r) // 2
            if (m*m < x or m*m == x) and (m+1)*(m+1) > x:
                return m
            elif m*m > x:
                r = m
            else:
                l = m