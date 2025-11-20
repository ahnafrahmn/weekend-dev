class Solution(object):
    def canMakeArithmeticProgression(self, arr):
        a = sorted(arr)
        pre, dif = a[0], a[1]-a[0]
        for i in a[1:]:
            if i-pre != dif:
                return False
            pre = i
        return True