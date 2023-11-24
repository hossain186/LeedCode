class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        new_s = "".join(i.lower() for i in s if i.isalnum())

        

        i = 0
        j = len(new_s)-1

        while i<=j:

            if new_s[i] != new_s[j]:
                return False

            i+=1
            j-=1

        return True