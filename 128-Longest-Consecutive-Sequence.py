class Solution:
    def longestConsecutive(self, n: List[int]) -> int:
        n[:] = sorted(set(n))
        r = m = 0
        for i in range(1, len(n)):
            if n[i]-n[i-1] == 1: r+=1
            else : 
                m = max(m, r)
                r = 0
        return 0 if len(n)==0 else max(m, r)+1