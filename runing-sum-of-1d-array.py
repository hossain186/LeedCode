class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        
        new = []

        total = 0
        for i in nums:
            total+=i

            new.append(total)

        return new