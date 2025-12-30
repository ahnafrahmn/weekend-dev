from collections import defaultdict
class Solution:
    def groupAnagrams(self, s: List[str]) -> List[List[str]]:
        r = defaultdict(list)
        for i in s:
            cnt = [0]*26
            for j in i: 
                cnt[ord(j)-ord('a')] += 1
            r[tuple(cnt)].append(i)
        return list(r.values())