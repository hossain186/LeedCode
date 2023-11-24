class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        result = 0

        for i in nums:

            c = nums.count(i)

            if c ==1:
                return i

        return result 