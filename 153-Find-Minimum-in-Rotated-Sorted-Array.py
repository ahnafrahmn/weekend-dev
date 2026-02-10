class Solution:
    def findMin(self, nums: List[int]) -> int:
        le = len(nums)
        if le < 3: return min(nums)
        l, r = 0, le-1
        while l <= r:
            m = (l+r)//2
            nl, nr, nm = nums[l], nums[r], nums[m]
            if nm < nums[m-1]: return nums[m]
            elif nl > nr:
                if nl > nm: r = m-1
                else: l = m+1
            else: r = m-1