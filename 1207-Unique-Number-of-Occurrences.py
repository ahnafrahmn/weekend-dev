class Solution(object):
    def uniqueOccurrences(self, arr):
        d = {}
        for i in arr:
            if i in d: d[i] = d[i]+1  
            else: d[i] = 1
        l=[]
        for i in d.values():
            l.append(i)
        return len(l)==len(set(l))