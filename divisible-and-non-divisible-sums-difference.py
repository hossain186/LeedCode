class Solution(object):
    def differenceOfSums(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        
        sum1 = 0
        sum2 = 0
        
        list1 = [i for i in range(1,n+1) if i%m!=0]
        list2 = [i for i in range(1,n+1) if i%m == 0]



        for i in  list1:
            sum1+=i

        for i in list2:
            sum2+=i

        return sum1-sum2