class Solution(object):
    def getSneakyNumbers(self, nums):
        r = []
        for i, j in enumerate(nums):
            if j in nums[i+1:]:
                r.append(j)
        return r
        