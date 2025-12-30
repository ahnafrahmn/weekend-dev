class Solution:
    def topKFrequent(self, n: List[int], k: int) -> List[int]:
        d = {}
        for i in n:
            if i not in d: d[i]=1
            else: d[i]+=1
        d = dict(sorted(d.items(), key=lambda x:x[1], reverse=True))

        return [key for key in list(d.keys())[:k]]