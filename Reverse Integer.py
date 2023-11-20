class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        a = x
        n = 2147483648-1

        if a>0:
            s = str(a)

            
            a = int(s[::-1])

            if a<= n:
                return a
            else:
                return 0



        else:
            a = abs(a)
            s = str(a)

            y = 0-int(s[::-1])

            if y>= (-2147483648):
                return y
            else:
                return 0
