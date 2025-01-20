class Solution:
    def isPalindrome(self, x: int) -> bool:
        xstr = str(x)
        rev = xstr[::-1]
        if xstr == rev:
            return True
        else:
            return False
        
