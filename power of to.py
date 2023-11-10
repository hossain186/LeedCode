class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        result = False
        for i in range(32):

            if 2**i == n:
                return True
                
            
        return result