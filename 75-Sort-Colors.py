class Solution(object):
    def sortColors(self, nums):
        z, o, t = [], [], []
        for i in nums:
            if i==2: t.append(i)
            elif i==1: o.append(i)
            else: z.append(i)
        nums[:]=z+o+t