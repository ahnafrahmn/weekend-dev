class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        res = max(piles)
        l, r = (sum(piles)+h-1)//h, res
        while l <= r:
            mid, summ = (l+r)//2, 0
            for p in piles: 
                summ += math.ceil(p / mid)
            if h >= summ: 
                res = min(res, mid)
                r = mid - 1
            else: 
                l = mid + 1
        return res 