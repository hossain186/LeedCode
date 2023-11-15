class Solution(object):
    def differenceOfSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        


        total= 0
        for i in nums:

            total+=i


        total2 = 0

        for i in nums:

            n = str(i)

            if len(n)>1:
                for j in n:
                    total2+=int(j)

            else:
                total2+=i


        return abs(total2-total)