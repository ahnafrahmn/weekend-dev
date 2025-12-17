class Solution(object):
    def letterCombinations(self, d):
        l = [ 
            '', '', 'abc', 'def', 
            'ghi', 'jkl', 'mno',
            'pqrs', 'tuv', 'wxyz'
        ]
        if len(d)==1:
            return list(l[int(d)])
        res = []
        def comb(r, n):
            if n == '':
                res.append(r)
                return
            for i in l[int(n[0])]:
                comb(r+i, n[1:])
        comb("", d)
        return res