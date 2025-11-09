def convertToTitle(self, n):
        s=''
        while n != 0:
            if n % 26 == 0:
                s = 'Z' + s
                n = int(n/26)-1
            else:
                s = chr(64 + int(n%26)) + s
                n = int(n/26)
        return s