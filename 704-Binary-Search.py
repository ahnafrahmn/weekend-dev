class Solution(object):
    def search(self, n, t):
        l, r = 0, len(n)-1
        if t not in n:
            return -1
        elif len(n) == 1 and n[0]==t:
            return 0
        while l < r:
            if l == r-1 and t > n[l] and t < n[r]:
                break 
            m = int((l+r+1)/2)
            if n[m] == t or n[l] == t or n[r] == t:
                return m if n[m]==t else l if n[l]==t else r
            elif n[m] < t:
                l = m
            else:
                r = m
        return -1
        