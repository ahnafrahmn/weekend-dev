from collections import Counter
class Solution:
    def equalFrequency(self, w: str) -> bool:
        s = sorted(Counter(w).values())
        return True if len(s)==1 or (len(s)==2 and s[0]==1) or s[-1]==1 or (s[-1]-1==s[-2] and s[0]==s[-2]) or (s[0]==1 and s[-1]==s[-2] and s[1]==s[-1]) else False