class Solution:
    def isPalindrome(self, x: int) -> bool:
    
        n = x
        revs = 0
        if(x<0):
            return False

        while x>0:

            remainder = x%10
            revs = (revs*10)+remainder
            x = x //10

        
        if revs == n:
            return True
        return False
    


