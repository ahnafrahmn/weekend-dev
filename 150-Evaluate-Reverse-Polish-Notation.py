class Solution(object):
    def evalRPN(self, t):
        r, signs = [], ["+", "-", "*", "/"]
        for i in t:
            if i not in signs:
                r.append(int(i))
            else:
                a, b = r[-2], r[-1]
                r.pop()
                r.pop()
                if i == "+":
                    r.append(a + b)
                elif i == "-":
                    r.append(a - b)
                elif i == "*":
                    r.append(a * b)
                else:
                    r.append(int(float(a) / b))
        return r[-1]