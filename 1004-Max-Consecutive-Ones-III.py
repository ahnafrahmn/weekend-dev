class Solution(object):
    def longestOnes(self, n, k):
        l = len(n)
        if sum(n)+k == l or (l==k):
            return l
        i = j = r = z = 0
        while j < l:
            z += 1 if n[j]==0 else 0
            while z > k:
                if n[i] == 0:
                    z -= 1
                i += 1
            j += 1
            r = max(j-i, r)
        return r