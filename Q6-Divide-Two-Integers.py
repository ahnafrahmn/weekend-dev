import math
def divide(self, a, b):
    s = 1 if (a < 0 and b < 0) or (a > 0 and b > 0) else -1
    a, b = abs(a), abs(b)
    if a < b:
        return 0
    elif b == 1:
        return a-1 if a*s == 2147483648 else a*s
    ans = int(math.pow(2.71828182845905, math.log(a)-math.log(b))) 
    return -ans if s == -1 else ans