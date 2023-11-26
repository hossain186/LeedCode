class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n == 0:
            return 0
        elif n ==1 or n == 2 :
            return 1
        
        result= 0
        a = 0
        b = 1
        for i in range(2,n+1):

            c = a+b
            a = b
            b =c
            
            result = c

            
        return result