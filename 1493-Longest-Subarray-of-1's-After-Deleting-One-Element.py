class Solution(object):
    def longestSubarray(self, n):
        l = len(n)
        if 0 not in n:
            return l-1
        elif 1 not in n:
            return 0
        i = z = 0
        r = None
        for j in range(l):
            if n[j]==0:
                z += 1
            if z > 1:
                r = max(r, j-i-1)
            while z > 1:
                if n[i]==0:
                    z -= 1
                i += 1
            if j == l-1 and r != None:
                r = max(r, j-i)
        return l-1 if r==None else r