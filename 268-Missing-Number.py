class Solution(object):
    def missingNumber(self, nums):
        for i, j in enumerate(sorted(nums)):
            if i != j:
                return i
        return len(nums)