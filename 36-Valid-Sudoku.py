class Solution:
    def isValidSudoku(self, b: List[List[str]]) -> bool:
        rows = [set() for t in range(9)]
        cols = [set() for t in range(9)]
        bxs = [set() for t in range(9)]
        for i in range(9):
            for j in range(9):
                k = b[i][j]
                if k == ".": continue
                bx = (i // 3) * 3 + (j // 3)
                if k in rows[i] or k in cols[j] or k in bxs[bx]: return False
                rows[i].add(k)
                cols[j].add(k)
                bxs[bx].add(k)
        return True