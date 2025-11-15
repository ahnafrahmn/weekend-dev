class Solution(object):
    def romanToInt(self, s):
        ro = {
            'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000
        }
        if len(s)==1:
            return ro[s[0]]
        i, r= len(s)-1, 0
        while i:
            pre = ro[s[i-1]]
            if pre < ro[s[i]]:
                r += (ro[s[i]] - pre)
                i -= 1
            else: 
                r += ro[s[i]]
            i -= 1
            if i == 0 or i < 0:
                return r + ro[s[0]] if i==0 else r