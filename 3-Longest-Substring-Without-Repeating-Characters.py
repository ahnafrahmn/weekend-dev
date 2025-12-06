class Solution(object):
    def lengthOfLongestSubstring(self, s):
        ss = {}
        maxx = i = j = 0
        while j < len(s):
            if s[j] in ss and ss[s[j]] >= i:
                i = ss[s[j]] + 1
            ss[s[j]] = j
            maxx = max(maxx, j - i + 1)
            j += 1
        return maxx