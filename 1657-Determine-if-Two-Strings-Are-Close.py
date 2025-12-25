from collections import Counter
class Solution:
    def closeStrings(self, x: str, y: str) -> bool:
        return set(x)==set(y) and len(x)==len(y) and sorted(Counter(x).values())==sorted(Counter(y).values())