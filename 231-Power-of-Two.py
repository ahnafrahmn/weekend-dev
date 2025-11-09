import math
class Solution(object):
    def isPowerOfTwo(self, n):
        if n < 1:
            return False
        return not (n & n-1)