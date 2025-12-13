class Solution(object):
    def maxFreqSum(self, s):
        v = "aeiou"
        dv, dc = {}, {}
        for c in s:
            if c in v:
                if c in dv:
                    dv[c] += 1
                else:
                    dv[c] = 1
            else:
                if c in dc:
                    dc[c] += 1
                else:
                    dc[c] = 1
        if len(dv)==0 or len(dc)==0:
            return max(dv.values()) if len(dc)==0 else max(dc.values())
        return max(dv.values()) + max(dc.values())