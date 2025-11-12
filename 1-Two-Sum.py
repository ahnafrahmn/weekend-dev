class Solution(object):
    def twoSum(self, n, t):
        for i, s in enumerate(n):
            try:
                j = n.index(t-s)
                if i==j:
                    continue
            except ValueError:
                continue
            else:
                return [i, j]
        