class Solution(object):
    def isValid(self, s):
        i = 0
        for c in s:
            if len(s)%2 == 1:
                return False
            elif i==len(s)-1:
                return True if s=="()" or s=="{}" or s=="[]" else False
            elif (c==')' and s[i-1]=='(') or (c==']' and s[i-1]=='[') or (c=='}' and s[i-1]=='{'):
                s = s[:i-1]+s[i+1:]
                i -= 2
            i += 1
        return False