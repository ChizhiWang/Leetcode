class Solution:
    def myAtoi(self, s: str) -> int:
        ans = 0
        k = 0
        for c in s:
            if k == 0:
                if c == ' ':
                    continue
                elif c == '-':
                    k = -1
                elif c == '+':
                    k = 1
                elif c >= '0' and c <= '9':
                    k = 1
                    ans = ans*10 + ord(c)- ord('0')
                else:
                    return k*ans
            else:
                if c >= '0' and c <= '9':
                    if k == 1 and ans > (pow(2,31)-1-(ord(c) - ord('0')))/10:
                        return pow(2,31)-1
                    elif k == -1 and ans > (pow(2,31)-(ord(c) - ord('0')))/10:
                        return -pow(2,31)
                    ans = ans*10 + ord(c) - ord('0')
                else:
                    return k*ans
        return k*ans




st = '-123'
print(Solution.myAtoi(Solution, st))