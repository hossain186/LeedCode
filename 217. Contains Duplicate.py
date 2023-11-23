class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        ex_nums = set()

        for i in nums:
            if i in ex_nums:
                return True
            
            ex_nums.add(i)
        return False        

        