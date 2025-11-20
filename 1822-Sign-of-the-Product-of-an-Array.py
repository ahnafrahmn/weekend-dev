class Solution(object):
    def signFunc(self, x):
        return 1 if x>0 else -1 if x<0 else 0
    def arraySign(self, nums):
        product = 1
        for i in nums:
            product *= i
        return self.signFunc(product)