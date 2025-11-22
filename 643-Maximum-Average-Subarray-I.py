class Solution(object):
    def findMaxAverage(self, n, k):
        l, s, i, j= len(n), sum(n[:k]), 0, k
        if l==k:
            return float(s)/k
        m = s
        while j < l:
            s = s-n[i]+n[j]
            if m < s:
                m = s
            i += 1
            j += 1
        return float(m)/k