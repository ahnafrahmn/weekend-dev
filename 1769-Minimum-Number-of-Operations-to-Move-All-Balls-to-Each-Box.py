class Solution(object):
    def minOperations(self, bxs):
        l , r = [], []
        ln = len(bxs)
        for i in range(ln):
            if bxs[i] == '1':
                l.append(i)
        for i in range(ln):
            t = 0
            for j in l:
                t += abs(i - j)
            r.append(t)
        return r