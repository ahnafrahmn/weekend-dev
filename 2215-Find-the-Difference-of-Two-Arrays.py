class Solution(object):
    def findDifference(self, n1, n2):
        n1, n2 = set(n1), set(n2)
        return [list(n1-n2), list(n2-n1)]