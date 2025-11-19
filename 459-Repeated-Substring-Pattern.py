class Solution(object):
    def repeatedSubstringPattern(self, s):
        l = len(s)
        if l==1:
            return False
        for i in range(1, l):
            if l%i==0 and s[i-1]==s[-1]:
                if s[:i]*(l//i) == s:
                    return True
        return False