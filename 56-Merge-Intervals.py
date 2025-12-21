class Solution(object):
    def merge(self, ls):
        i = 1
        ls.sort()
        res = [ls[0]]
        for x, y in ls[1:]:
            if res[-1][1] >= x:
                res[-1][1] = max(y, res[-1][1])
            else: 
                res.append([x, y])
        return res if len(ls)>1 else ls