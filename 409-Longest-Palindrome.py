class Solution(object):
    def longestPalindrome(self, s):
        d = {}
        for i in s:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        d = dict(sorted(d.items(), key=lambda x:x[1], reverse=True))
        odd = res = 0
        for i in d.values():
            if i%2:
                if odd:
                    res += i-1
                else:
                    odd += 1
                    res += i
            else:
                res += i
        return res