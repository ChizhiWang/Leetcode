class Solution:
    def convert(self, s: str, numRows: int) -> str:
        n = len(s)
        if numRows == 1:
            return s
        k = 2*numRows-2
        m = n//k
        ans = ''
        for i in range(numRows):
            for j in range(m):
                if i==0 or i == numRows-1 :
                    ans = ans + s[j*k+i]
                else:
                    ans = ans + s[j*k+i] + s[(j+1)*k-i]
            if m*k+i < n:
                ans = ans + s[m*k+i]
            if (m+1)*k-i < n and i != numRows-1:
                ans = ans + s[(m+1)*k-i]
        return ans

st = 'ABC'
n = 3
print(Solution.convert(Solution, s = st, numRows = 3))
