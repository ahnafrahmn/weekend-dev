class Solution(object):
    def containsNearbyDuplicate(self, n, k):
        l = len(n)
        if k==0 or l==len(set(n)): 
            return False
        for i in range(l):
            if n[i] in n[i-k:i] or n[i] in n[i+1:i+k+1]:
                return True
        return False