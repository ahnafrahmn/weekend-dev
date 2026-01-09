class Solution:
    def threeSum(self, n: List[int]) -> List[List[int]]:
        n[:] = sorted(n)
        l, res = len(n), []
        if n[l-1] < 0: return res
        for i in range(l):
            if n[i] > 0: break
            if i>0 and n[i]==n[i-1]: continue
            t, j, k = n[i], i+1, l-1
            while j<k:
                s = t + n[j] + n[k]
                if s < 0: j += 1
                elif s > 0: k -= 1
                else: 
                    res.append([t, n[j], n[k]])
                    j += 1
                    k -= 1
                    while j<k and n[j]==n[j-1]: j+=1
                    while j<k and n[k]==n[k+1]: k-=1
        return res