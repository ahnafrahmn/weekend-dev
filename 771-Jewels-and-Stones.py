class Solution(object):
    def numJewelsInStones(self, j, s):
        r = 0
        for i in range(len(s)):
            r += 1 if s[i] in j else 0
        return r