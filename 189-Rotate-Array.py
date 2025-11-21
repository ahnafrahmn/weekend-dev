class Solution(object):
    def rotate(self, a, k):
        k = k%len(a) if k > len(a) else k
        a[:] = a[-k:]+a[:-k]
        return a