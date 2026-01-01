class Solution:
    def evalRPN(self, t: List[str]) -> int:
        r = []
        for i in range(len(t)):
            if t[i] in '+-*/': 
                a, b = r[-2], r[-1]
                r.pop()
                r.pop()
                if t[i]=='+': r.append(a+b)
                elif t[i]=='-': r.append(a-b)
                elif t[i]=='*': r.append(a*b)
                else: r.append(int(a/b))
            else: r.append(int(t[i]))
        return r[-1]