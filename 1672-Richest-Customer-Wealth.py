class Solution(object):
    def maximumWealth(self, ac):
        r = 0
        for i in ac:
            r = max(r, sum(i))
        return r