class Solution:
    def dailyTemperatures(self, t: List[int]) -> List[int]:
        ans, st, l = [0]*len(t), [], len(t)
        if l==1: return [0]
        for i in range(l):
            while st and t[i] > st[-1][0]:
                val, idx = st.pop()
                ans[idx] = i - idx
            st.append([t[i], i])
        return ans