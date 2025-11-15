class Solution(object):
    def twoSum(self, n, t):
        s = sorted(list(set(n)))
        for i, j in enumerate(s):
            if t == j and j == 0:
                return [n.index(j)+1, n.index(j)+2]
            elif t-j in n:
                return [n.index(j)+1, n.index(t-j)+2] if n[n.index(j)] == n[n.index(j)+1] and n[n.index(j)]+n[n.index(j)+1]==t else [n.index(j)+1, n.index(t-j)+1]