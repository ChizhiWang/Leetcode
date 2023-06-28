class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            k = 1
        else:
            k = -1
            x = -x
        ans = 0
        while x < 0:
            r = (10-x%10)%10
            if ans < (-pow(2,31)+r)/10:
                return 0
            ans = ans*10-r
            if r == 0:
                x = x//10
            else:
                x = x//10+1
        if k < 0 and ans <= -pow(2,31):
            return 0
        return ans*k


xx = 120
print(Solution.reverse(Solution, xx))
    
