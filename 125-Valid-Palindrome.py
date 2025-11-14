class Solution(object):
    def isPalindrome(self, s):
        r = set('abcdefghijklmnopqrstuvwxyz0123456789')
        x = ''.join([i for i in s.lower() if i in r])
        return x == x[::-1]