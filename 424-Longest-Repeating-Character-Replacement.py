class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        l, m, res, le, mchar = 0, 1, 1, len(s), s[0]
        if le == 1: return 1
        if len(set(s))==1: return le
        for i, r in enumerate(s):
            if r not in freq: freq[r] = 1
            else:
                freq[r] += 1
                if m < freq[r]: 
                    m = freq[r]
                    mchar = r
            if (i-l+1)-m > k:
                if i-l > res: res = i-l
                freq[s[l]] -= 1
                if mchar == s[l]: m -= 1 
                l += 1
        if (le-l)-m <= k: return le-l
        return res if le-m > k else le   