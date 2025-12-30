class Solution:
    def productExceptSelf(self, n: List[int]) -> List[int]:
        s = len(n)
        r = [1]*s
        for i in range(1, s):
            r[i] = r[i-1] * n[i-1]
        t=1
        for i in range(s-1, -1, -1):
            r[i] *= t
            t *= n[i]
        return r