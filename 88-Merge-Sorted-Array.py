class Solution(object):
    def merge(self, n1, m, n2, n):
        i, j, k = m-1, n-1, m+n-1
        while k >= 0:
            if i>0 and n1[i] >= n2[j]:
                n1[k] = n1[i]
                i -= 1
            else:
                n1[k] = n2[j]
                j -= 1
            k -= 1