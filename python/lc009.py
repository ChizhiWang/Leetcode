class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = ''
        if x == 0:
            return True
        elif x < 0:
            return False
        while x > 0:
            r = x%10
            s = s + chr(r)
            x = x//10
        i = 0
        j = len(s)-1
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True

# We can also reverse the number and check if it equals the original